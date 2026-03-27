import json
import csv
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/products')
def products():
    # on récupère les paramètres de l'URL
    source = request.args.get('source')
    product_id = request.args.get('id', type=int)
    data = []

    if source == 'json':
        # on ouvre et on lit le fichier JSON
        with open('products.json') as f:
            data = json.load(f)
    elif source == 'csv':
        # on ouvre le CSV et on convertit chaque ligne en dict
        with open('products.csv') as f:
            reader = csv.DictReader(f)
            for row in reader:
                data.append({'id': int(row['id']), 'name': row['name'],
                             'category': row['category'], 'price': float(row['price'])})
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
    app.run(debug=True, port=5000)