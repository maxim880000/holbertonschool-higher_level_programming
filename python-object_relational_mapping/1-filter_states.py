#!/usr/bin/python3
"""
Module pour filtrer les états commençant par 'N'.

Ce script se connecte à une base de données MySQL et récupère
uniquement les états dont le nom commence par la lettre 'N' majuscule.
Les résultats sont triés par ID.
"""

import MySQLdb
import sys


def filter_states_by_n(username, password, database):
    """
    Liste les états dont le nom commence par 'N'.

    Cette fonction utilise une clause WHERE avec LIKE pour filtrer
    les états. Le motif 'N%' signifie : commence par N, suivi de n'importe
    quoi (% = joker pour 0 ou plusieurs caractères).

    Args:
        username (str): Nom d'utilisateur MySQL
        password (str): Mot de passe MySQL
        database (str): Nom de la base de données

    Explication du filtre:
        - WHERE name LIKE 'N%' : filtre les noms commençant par 'N'
        - BINARY : rend la comparaison sensible à la casse
        - Sans BINARY, 'nevada' et 'Nevada' seraient tous deux acceptés
        - Avec BINARY, seul 'Nevada' (N majuscule) est accepté
    """
    # Connexion à la base MySQL sur localhost:3306
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database,
        charset="utf8"
    )

    # Création du curseur pour exécuter les requêtes
    cursor = db.cursor()

    # Requête SQL avec filtre WHERE
    # BINARY assure que seul 'N' majuscule est considéré (pas 'n')
    # 'N%' signifie : commence par N, puis n'importe quels caractères
    # ORDER BY id ASC : tri par ID en ordre croissant
    cursor.execute(
        "SELECT * FROM states WHERE BINARY name LIKE 'N%' ORDER BY id ASC"
    )

    # Récupération de tous les résultats correspondant au filtre
    rows = cursor.fetchall()

    # Affichage de chaque état trouvé
    for row in rows:
        print(row)

    # Libération des ressources
    cursor.close()
    db.close()


if __name__ == "__main__":
    """
    Point d'entrée du script.

    Exécute le filtre avec les arguments fournis en ligne de commande.
    """
    filter_states_by_n(sys.argv[1], sys.argv[2], sys.argv[3])
