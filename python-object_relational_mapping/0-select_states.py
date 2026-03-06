#!/usr/bin/python3
"""
Module pour lister tous les états de la base de données.

Ce script se connecte à une base de données MySQL et récupère
tous les états de la table 'states', triés par ID croissant.
Utilise MySQLdb pour une connexion directe à MySQL.
"""

import MySQLdb
import sys


def list_all_states(username, password, database):
    """
    Liste tous les états de la base de données.

    Cette fonction établit une connexion à MySQL, exécute une requête
    SELECT pour récupérer tous les états triés par ID, puis affiche
    chaque résultat sous forme de tuple.

    Args:
        username (str): Nom d'utilisateur MySQL
        password (str): Mot de passe MySQL
        database (str): Nom de la base de données à interroger

    Processus:
        1. Connexion au serveur MySQL sur localhost:3306
        2. Création d'un curseur pour exécuter les requêtes
        3. Exécution de la requête SELECT avec ORDER BY
        4. Récupération de tous les résultats
        5. Affichage ligne par ligne
        6. Fermeture du curseur et de la connexion
    """
    # Connexion à la base de données MySQL
    # host="localhost" : serveur MySQL local
    # port=3306 : port par défaut de MySQL
    # user : nom d'utilisateur fourni en argument
    # passwd : mot de passe fourni en argument
    # db : nom de la base de données
    # charset="utf8" : encodage pour gérer les caractères spéciaux
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database,
        charset="utf8"
    )

    # Création d'un curseur pour exécuter les requêtes SQL
    # Le curseur permet de parcourir les résultats d'une requête
    cursor = db.cursor()

    # Exécution de la requête SQL
    # SELECT * FROM states : sélectionne toutes les colonnes de la table
    # ORDER BY id ASC : trie les résultats par ID en ordre croissant
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # Récupération de tous les résultats de la requête
    # fetchall() retourne une liste de tuples, chaque tuple = une ligne
    rows = cursor.fetchall()

    # Affichage de chaque état sous forme de tuple
    # Chaque ligne contient (id, name) de la table states
    for row in rows:
        print(row)

    # Fermeture du curseur pour libérer les ressources
    cursor.close()

    # Fermeture de la connexion à la base de données
    db.close()


if __name__ == "__main__":
    """
    Point d'entrée du script.

    Vérifie que le script est exécuté directement (pas importé),
    puis appelle la fonction avec les arguments de la ligne de commande.

    Arguments attendus:
        sys.argv[1] : nom d'utilisateur MySQL
        sys.argv[2] : mot de passe MySQL
        sys.argv[3] : nom de la base de données
    """
    # Appel de la fonction avec les arguments du terminal
    # sys.argv[0] est le nom du script
    # sys.argv[1], [2], [3] sont les arguments fournis
    list_all_states(sys.argv[1], sys.argv[2], sys.argv[3])
