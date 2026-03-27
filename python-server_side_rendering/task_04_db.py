import json
import csv
import sqlite3
from flask import Flask, render_template, request

app = Flask(__name__)


def create_database():
    # connexion au fichier SQLite (le crée s'il n'existe pas)
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()
    # on crée la table si elle n'existe pas encore
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Products (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            category TEXT NOT NULL,
            price REAL NOT NULL
        )
    ''')
    # on insère les données de test
    cursor.execute('''
        INSERT OR IGNORE INTO Products (id, name, category, price)
        VALUES
        (1, 'Laptop', 'Electronics', 799.99),
        (2, 'Coffee Mug', 'Home Goods', 15.99)
    ''')
    conn.commit()
    conn.close()


@app.route('/products')
def products():
    # on récupère les paramètres de l'URL
    source = request.args.get('source')
    product_id = request.args.get('id', type=int)
    data = []

    if source == 'json':
        # lecture du fichier JSON
        with open('products.json') as f:
            data = json.load(f)
    elif source == 'csv':
        # lecture du fichier CSV ligne par ligne
        with open('products.csv') as f:
            reader = csv.DictReader(f)
            for row in reader:
                data.append({'id': int(row['id']), 'name': row['name'],
                             'category': row['category'], 'price': float(row['price'])})
    elif source == 'sql':
        # on interroge la base SQLite
        conn = sqlite3.connect('products.db')
        conn.row_factory = sqlite3.Row  # pour avoir des résultats comme des dicts
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM Products')
        data = [dict(row) for row in cursor.fetchall()]
        conn.close()
    else:
        # source inconnue
        return render_template('product_display.html', error="Wrong source")

    if product_id is not None:
        # on filtre par id si demandé
        data = [p for p in data if p['id'] == product_id]
        if not data:
            return render_template('product_display.html', error="Product not found")

    return render_template('product_display.html', products=data)


if __name__ == '__main__':
    create_database()
    app.run(debug=True, port=5000)
