#!/usr/bin/python3
"""Lists states by name using user input - UNSAFE (SQL injection possible)."""

import MySQLdb
import sys


def filter_by_user_input(username, password, database, state_name):
    """Connect to MySQL and print states matching state_name (unsafe).

    WARNING: state_name is inserted directly into the query via .format(),
    which allows SQL injection attacks. See task 3 for the safe version.
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
    # DANGEREUX : .format() insère l'input directement sans échappement
    query = "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC".format(
        state_name
    )
    cursor.execute(query)

    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    db.close()


if __name__ == "__main__":
    # sys.argv[1]=user  [2]=password  [3]=database  [4]=state_name
    filter_by_user_input(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
