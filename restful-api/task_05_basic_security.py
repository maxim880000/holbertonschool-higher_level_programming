from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import (
    JWTManager,
    create_access_token,
    jwt_required,
    get_jwt
)
from werkzeug.security import generate_password_hash, check_password_hash


app = Flask(__name__)

# Clé secrète utilisée pour signer et vérifier les tokens JWT
# En production, utiliser une vraie clé longue et aléatoire
app.config["JWT_SECRET_KEY"] = "super-secret-key-change-in-production"

# Initialisation des deux systèmes d'authentification
auth = HTTPBasicAuth()   # pour le Basic Auth (username:password encodé en base64)
jwt  = JWTManager(app)   # pour les tokens JWT


# Base d'utilisateurs stockée en mémoire (dict Python)
# Les mots de passe sont hashés avec werkzeug pour ne jamais stocker en clair
users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user"
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin"
    }
}


# BASIC AUTHENTICATION

# Cette fonction est appelée automatiquement par @auth.login_required
# Elle reçoit le username et password extraits de l'en-tête Authorization
# Elle doit retourner le username si valide, ou None si invalide
@auth.verify_password
def verify_password(username, password):
    user = users.get(username)
    if user and check_password_hash(user["password"], password):
        return username
    return None


# Route protégée par Basic Auth
# Si l'utilisateur n'envoie pas de credentials valides, 401 est retourné automatiquement
@app.route("/basic-protected")
@auth.login_required
def basic_protected():
    return jsonify("Basic Auth: Access Granted")


# JWT AUTHENTICATION

# Route de login : l'utilisateur envoie username + password en JSON
# En retour il reçoit un token JWT qu'il utilisera pour les requêtes suivantes
@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()

    if not data:
        return jsonify({"error": "Missing JSON body"}), 400

    username = data.get("username")
    password = data.get("password")

    user = users.get(username)

    # Vérification du mot de passe avec check_password_hash (compare avec le hash stocké)
    if not user or not check_password_hash(user["password"], password):
        return jsonify({"error": "Invalid credentials"}), 401

    # On embarque le rôle dans le payload du token pour pouvoir le vérifier plus tard
    # sans retourner chercher dans la base à chaque requête
    additional_claims = {"role": user["role"]}
    access_token = create_access_token(identity=username, additional_claims=additional_claims)

    return jsonify({"access_token": access_token})


# Route protégée par JWT
# Le client doit envoyer le token dans le header : Authorization: Bearer <token>
# Sans token valide, nos handlers en bas retournent 401
@app.route("/jwt-protected")
@jwt_required()
def jwt_protected():
    return jsonify("JWT Auth: Access Granted")


# Route accessible uniquement aux admins
# On récupère les claims du token (le payload) et on vérifie le rôle
@app.route("/admin-only")
@jwt_required()
def admin_only():
    claims = get_jwt()

    if claims.get("role") != "admin":
        return jsonify({"error": "Admin access required"}), 403

    return jsonify("Admin Access: Granted")


# GESTIONNAIRES D'ERREURS JWT
# Flask-JWT-Extended appelle ces fonctions quand il détecte une anomalie sur le token
# Le projet exige que TOUTES les erreurs d'auth retournent 401


# Token absent ou header Authorization manquant
@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    return jsonify({"error": "Missing or invalid token"}), 401


# Token présent mais syntaxiquement invalide (corrompu, mauvais format...)
@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    return jsonify({"error": "Invalid token"}), 401


# Token valide mais dont la date d'expiration est dépassée
# Attention : Flask-JWT >= 4.x passe 2 arguments (jwt_header, jwt_data)
@jwt.expired_token_loader
def handle_expired_token_error(jwt_header, jwt_data):
    return jsonify({"error": "Token has expired"}), 401


# Token qui a été explicitement révoqué (blacklist)
# Attention : Flask-JWT >= 4.x passe 2 arguments (jwt_header, jwt_data)
@jwt.revoked_token_loader
def handle_revoked_token_error(jwt_header, jwt_data):
    return jsonify({"error": "Token has been revoked"}), 401


# Une route demande un token "frais" (fresh=True) mais le token fourni ne l'est pas
@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(jwt_header, jwt_data):
    return jsonify({"error": "Fresh token required"}), 401


if __name__ == "__main__":
    app.run(debug=True)
