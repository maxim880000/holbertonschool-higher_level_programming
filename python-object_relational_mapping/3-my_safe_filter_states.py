#!/usr/bin/python3
"""Lists states by name - safe version using parameterized queries."""

import MySQLdb
import sys


def safe_filter_by_input(username, password, database, state_name):
    """Connect to MySQL and print states matching state_name (safe).

    Uses %s placeholder instead of .format() so MySQLdb escapes
    special characters automatically, preventing SQL injection.
    """
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database,
        charset="utf8"
    )

    cursor = db.cursor()
    # %s est remplacé par state_name de façon sécurisée par MySQLdb
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    cursor.execute(query, (state_name,))  # (state_name,) = tuple à 1 élément

    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    db.close()


if __name__ == "__main__":
    # sys.argv[1]=user  [2]=password  [3]=database  [4]=state_name
    safe_filter_by_input(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
