#!/usr/bin/python3
"""
Module pour lister toutes les villes avec leur état.

Ce script effectue une jointure SQL (JOIN) entre les tables
'cities' et 'states' pour afficher chaque ville avec le nom
de son état correspondant.
"""

import MySQLdb
import sys


def list_cities_by_state(username, password, database):
    """
    Liste toutes les villes avec leur état associé.

    Cette fonction utilise un JOIN SQL pour combiner les données
    de deux tables : 'cities' et 'states'. Le JOIN permet de récupérer
    en une seule requête les informations des deux tables.

    Args:
        username (str): Nom d'utilisateur MySQL
        password (str): Mot de passe MySQL
        database (str): Nom de la base de données

    Structure des tables :
        states:
            - id (clé primaire)
            - name
        
        cities:
            - id (clé primaire)
            - state_id (clé étrangère vers states.id)
            - name

    Fonctionnement du JOIN :
        SELECT cities.id, cities.name, states.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        
        Explication ligne par ligne :
        1. SELECT cities.id, cities.name, states.name
           → Colonnes à récupérer : ID de la ville, nom de la ville, nom de l'état
        
        2. FROM cities
           → Table principale : cities
        
        3. JOIN states ON cities.state_id = states.id
           → Pour chaque ville, trouver l'état correspondant
           → cities.state_id doit correspondre à states.id
           → Cela crée une "liaison" entre les deux tables
        
        4. ORDER BY cities.id ASC
           → Trier par ID de ville en ordre croissant

    Exemple de résultat :
        (1, 'San Francisco', 'California')
        (2, 'San Jose', 'California')
        (6, 'Page', 'Arizona')
    """
    # Connexion à la base de données
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database,
        charset="utf8"
    )

    cursor = db.cursor()

    # Requête SQL avec JOIN pour combiner cities et states
    # Le JOIN lie cities.state_id avec states.id
    # Cela permet d'obtenir le nom de l'état pour chaque ville
    query = """
        SELECT cities.id, cities.name, states.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        ORDER BY cities.id ASC
    """
    
    # Exécution de la requête (une seule fois comme demandé)
    cursor.execute(query)

    # Récupération de tous les résultats
    # Chaque ligne contient : (id_ville, nom_ville, nom_état)
    rows = cursor.fetchall()

    # Affichage de chaque ville avec son état
    for row in rows:
        print(row)

    cursor.close()
    db.close()


if __name__ == "__main__":
    """
    Point d'entrée du script.

    Affiche toutes les villes avec leur état en utilisant
    une jointure SQL efficace.
    """
    list_cities_by_state(sys.argv[1], sys.argv[2], sys.argv[3])
