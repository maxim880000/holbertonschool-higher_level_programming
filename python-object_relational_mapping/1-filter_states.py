#!/usr/bin/python3
"""Lists all states whose name starts with 'N' using MySQLdb."""

import MySQLdb
import sys


def filter_states_by_n(username, password, database):
    """Connect to MySQL and print states starting with 'N' ordered by id."""
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database,
        charset="utf8"
    )

    cursor = db.cursor()
    # BINARY rend la comparaison sensible à la casse (N ≠ n)
    cursor.execute(
        "SELECT * FROM states WHERE BINARY name LIKE 'N%' ORDER BY id ASC"
    )

    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    db.close()


if __name__ == "__main__":
    # sys.argv[1]=user  [2]=password  [3]=database
    filter_states_by_n(sys.argv[1], sys.argv[2], sys.argv[3])