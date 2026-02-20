#!/usr/bin/python3
"""
API Flask simple pour gérer des utilisateurs
"""

# Import des outils Flask nécessaires
from flask import Flask, jsonify, request

# Création de l'application Flask
app = Flask(__name__)

# Dictionnaire pour stocker les utilisateurs en mémoire
# Clé = username, Valeur = objet utilisateur complet
users = {}


# Route principale - Page d'accueil
@app.route("/")
def home():
    """Retourne un message de bienvenue"""
    return "Welcome to the Flask API!"


# Route pour vérifier que l'API fonctionne
@app.route("/status")
def status():
    """Retourne OK si le serveur fonctionne"""
    return "OK"


# Route pour obtenir la liste de tous les usernames
@app.route("/data")
def get_data():
    """Retourne la liste des noms d'utilisateurs"""
    # Récupère uniquement les clés (usernames) du dictionnaire
    usernames = list(users.keys())
    return jsonify(usernames)


# Route dynamique pour obtenir un utilisateur spécifique
@app.route("/users/<username>")
def get_user(username):
    """
    Retourne les informations d'un utilisateur
    Si l'utilisateur n'existe pas, retourne une erreur 404
    """
    # Cherche l'utilisateur dans le dictionnaire
    user = users.get(username)
    
    # Si l'utilisateur n'existe pas
    if user is None:
        return jsonify({"error": "User not found"}), 404
    
    # Retourne les données de l'utilisateur
    return jsonify(user)


# Route pour ajouter un nouvel utilisateur (méthode POST)
@app.route("/add_user", methods=["POST"])
def add_user():
    """
    Ajoute un nouvel utilisateur à l'API
    Vérifie que les données sont valides avant d'ajouter
    """
    # Essaie de récupérer les données JSON envoyées
    try:
        data = request.get_json()
    except:
        # Si le JSON est invalide, retourne une erreur 400
        return jsonify({"error": "Invalid JSON"}), 400
    
    # Vérifie que les données ne sont pas vides
    if data is None:
        return jsonify({"error": "Invalid JSON"}), 400
    
    # Vérifie que le username est présent
    if "username" not in data:
        return jsonify({"error": "Username is required"}), 400
    
    username = data["username"]
    
    # Vérifie que le username n'existe pas déjà
    if username in users:
        return jsonify({"error": "Username already exists"}), 409
    
    # Ajoute l'utilisateur au dictionnaire
    users[username] = data
    
    # Retourne un message de confirmation avec code 201 (Created)
    return jsonify({
        "message": "User added",
        "user": data
    }), 201


# Lance le serveur Flask en mode développement
if __name__ == "__main__":
    app.run()