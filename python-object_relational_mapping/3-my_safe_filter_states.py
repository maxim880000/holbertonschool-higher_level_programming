#!/usr/bin/python3
"""
Module pour rechercher un état par nom (VERSION SÉCURISÉE).

✅ Ce script utilise les requêtes paramétrées pour se protéger
contre les injections SQL. L'input utilisateur est traité comme
une valeur, jamais comme du code SQL exécutable.
"""

import MySQLdb
import sys


def safe_filter_by_input(username, password, database, state_name):
    """
    Recherche un état par nom de manière sécurisée.

    ✅ SÉCURISÉ : Cette fonction utilise des paramètres (%s) au lieu de
    .format() pour construire la requête. MySQLdb échappe automatiquement
    les caractères spéciaux, empêchant les injections SQL.

    Args:
        username (str): Nom d'utilisateur MySQL
        password (str): Mot de passe MySQL
        database (str): Nom de la base de données
        state_name (str): Nom de l'état à rechercher (SÉCURISÉ)

    Protection contre les injections :
        Au lieu de : "SELECT * FROM states WHERE name = '{}'".format(state_name)
        On utilise : "SELECT * FROM states WHERE name = %s" + (state_name,)
        
        Différence cruciale :
        - Avec .format() : l'input est inséré TEL QUEL dans la requête
        - Avec %s et tuple : MySQLdb traite l'input comme une VALEUR
        
        Exemple d'attaque bloquée :
        Input : "Arizona'; DROP TABLE states; --"
        
        Avec .format() (dangereux) :
            Requête : SELECT * FROM states WHERE name = 'Arizona'; DROP TABLE states; --'
            Résultat : Exécute DROP TABLE (catastrophe !)
        
        Avec %s (sécurisé) :
            Requête : SELECT * FROM states WHERE name = 'Arizona''; DROP TABLE states; --'
            Résultat : Cherche littéralement cet état (aucun état trouvé, mais pas de dégâts)
            Les caractères spéciaux (apostrophes, points-virgules) sont échappés
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

    # ✅ LIGNE SÉCURISÉE : Utilisation de paramètres avec %s
    # La requête contient un placeholder %s au lieu de la valeur directe
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"

    # Le second argument de execute() est un tuple contenant les valeurs
    # MySQLdb remplace %s par state_name en échappant les caractères dangereux
    # (state_name,) crée un tuple avec un seul élément (la virgule est importante)
    cursor.execute(query, (state_name,))

    # Récupération et affichage des résultats
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    db.close()


if __name__ == "__main__":
    """
    Point d'entrée du script.

    Utilisation sécurisée de l'input utilisateur grâce aux
    requêtes paramétrées dans la fonction safe_filter_by_input().
    """
    safe_filter_by_input(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
