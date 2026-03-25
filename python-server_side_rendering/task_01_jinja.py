#!/usr/bin/env python3
"""
Task 01 - Application Flask basique avec templates Jinja
Ce module crée un serveur web Flask qui sert plusieurs pages HTML
en utilisnt le moteur de templates Jinja
"""

from flask import Flask, render_template

# Création de l'instance Flask
# __name__ permet à Flask de localiser le dossier templates/ automatiquement
app = Flask(__name__)


@app.route('/')
def home():
    """Route principale - affiche la page d'accueil (index.html)."""
    return render_template('index.html')


@app.route('/about')
def about():
    """Route /about - affiche la page 'À propos' (about.html)."""
    return render_template('about.html')


@app.route('/contact')
def contact():
    """Route /contact - affiche la page de contact (contact.html)."""
    return render_template('contact.html')


# Point d'entrée : lance le serveur en mode debug sur le port 5000
if __name__ == '__main__':
    app.run(debug=True, port=5000)