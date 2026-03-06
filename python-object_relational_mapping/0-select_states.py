#!/usr/bin/python3
"""Lists all states from the database using MySQLdb."""

import MySQLdb
import sys


def list_all_states(username, password, database):
    """Connect to MySQL and print all states ordered by id."""
    # Connexion au serveur MySQL local (port 3306 par défaut)
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database,
        charset="utf8"
    )

    cursor = db.cursor()
    # Récupère toutes les lignes de la table states, triées par id
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    rows = cursor.fetchall()  # liste de tuples (id, name)

    for row in rows:
        print(row)

    cursor.close()
    db.close()


if __name__ == "__main__":
    # sys.argv[1]=user  [2]=password  [3]=database
    list_all_states(sys.argv[1], sys.argv[2], sys.argv[3])
