#!/usr/bin/python3
"""
Module pour rechercher un état par nom (VERSION NON SÉCURISÉE).

⚠️ ATTENTION : Ce script est vulnérable aux injections SQL !
Il utilise .format() pour insérer directement l'input utilisateur
dans la requête SQL, ce qui permet des attaques malveillantes.

Exemple d'attaque :
    Input : "Arizona'; TRUNCATE TABLE states; SELECT * FROM states WHERE name = '"
    Résultat : Suppression de toute la table !
"""

import MySQLdb
import sys


def filter_by_user_input(username, password, database, state_name):
    """
    Recherche un état par nom en utilisant l'input utilisateur.

    ⚠️ VULNÉRABILITÉ : Cette fonction utilise .format() pour construire
    la requête SQL. Un utilisateur malveillant peut injecter du code SQL
    arbitraire dans le paramètre state_name.

    Args:
        username (str): Nom d'utilisateur MySQL
        password (str): Mot de passe MySQL
        database (str): Nom de la base de données
        state_name (str): Nom de l'état à rechercher (NON SÉCURISÉ)

    Problème de sécurité :
        La ligne query = "SELECT ... '{}'".format(state_name)
        insère directement state_name dans la requête SQL.
        
        Si state_name = "Texas" : OK, requête normale
        Si state_name = "x'; DROP TABLE states; --" : DANGER !
        La requête devient : SELECT * FROM states WHERE name = 'x';
                             DROP TABLE states; --'
        
        Cela exécute deux commandes :
        1. SELECT... (normal)
        2. DROP TABLE states (suppression de la table !)
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

    # ⚠️ LIGNE DANGEREUSE : Construction de la requête avec .format()
    # L'input utilisateur est directement inséré dans la chaîne SQL
    # sans aucune validation ou échappement des caractères spéciaux
    query = "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC".format(
        state_name
    )

    # Exécution de la requête potentiellement dangereuse
    cursor.execute(query)

    # Récupération et affichage des résultats
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    db.close()


if __name__ == "__main__":
    """
    Point d'entrée du script.

    Reçoit 4 arguments :
        sys.argv[1] : nom d'utilisateur MySQL
        sys.argv[2] : mot de passe MySQL
        sys.argv[3] : nom de la base de données
        sys.argv[4] : nom de l'état à rechercher (DANGEREUX si non validé)
    """
    filter_by_user_input(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
