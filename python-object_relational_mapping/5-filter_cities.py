#!/usr/bin/python3
"""
Module pour lister les villes d'un état spécifique.

Ce script prend un nom d'état en paramètre et affiche toutes
les villes de cet état, séparées par des virgules.
Protégé contre les injections SQL.
"""

import MySQLdb
import sys


def filter_cities_by_state(username, password, database, state_name):
    """
    Liste toutes les villes d'un état donné.

    Utilise un JOIN sécurisé avec paramètres pour éviter les injections SQL.
    Les noms de villes sont affichés sur une seule ligne, séparés par des virgules.

    Args:
        username (str): Nom d'utilisateur MySQL
        password (str): Mot de passe MySQL
        database (str): Nom de la base de données
        state_name (str): Nom de l'état dont on veut les villes

    Fonctionnement :
        1. JOIN entre cities et states pour lier les tables
        2. WHERE states.name = %s pour filtrer par nom d'état
        3. ORDER BY cities.id pour trier les villes
        4. Affichage des villes séparées par ", " (virgule + espace)

    Gestion du format d'affichage :
        - Si état trouvé avec villes : "Dallas, Houston, Austin"
        - Si état trouvé sans villes ou état non trouvé : ligne vide
        
        La méthode join() assemble une liste en une chaîne :
        ['Dallas', 'Houston', 'Austin'] → "Dallas, Houston, Austin"
        
        row[0] correspond à cities.name (première colonne du SELECT)
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

    # Requête sécurisée avec paramètre %s
    # Le JOIN lie cities à states via cities.state_id = states.id
    # Le WHERE filtre par nom d'état (paramètre sécurisé)
    query = """
        SELECT cities.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        WHERE states.name = %s
        ORDER BY cities.id ASC
    """
    
    # Exécution avec paramètre sécurisé (protection contre injections SQL)
    # (state_name,) crée un tuple avec un seul élément
    cursor.execute(query, (state_name,))

    # Récupération de tous les résultats
    rows = cursor.fetchall()

    # Extraction des noms de villes dans une liste
    # row[0] car on ne sélectionne qu'une colonne (cities.name)
    # Compréhension de liste : [row[0] for row in rows]
    # Signifie : pour chaque row dans rows, prendre row[0]
    city_names = [row[0] for row in rows]

    # Affichage des villes séparées par ", "
    # join() assemble les éléments d'une liste en une chaîne
    # Exemple : ['A', 'B', 'C'] avec ", ".join() → "A, B, C"
    # Si la liste est vide, join() retourne une chaîne vide ""
    print(", ".join(city_names))

    cursor.close()
    db.close()


if __name__ == "__main__":
    """
    Point d'entrée du script.

    Affiche les villes d'un état spécifique, protégé contre
    les injections SQL grâce aux requêtes paramétrées.
    """
    filter_cities_by_state(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
