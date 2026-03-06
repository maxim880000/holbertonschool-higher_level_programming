#!/usr/bin/python3
"""Lists all cities of a given state, displayed as a comma-separated line."""

import MySQLdb
import sys


def filter_cities_by_state(username, password, database, state_name):
    """Connect to MySQL and print cities of state_name separated by commas."""
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database,
        charset="utf8"
    )

    cursor = db.cursor()
    # JOIN + WHERE sécurisé via %s pour éviter les injections SQL
    query = """
        SELECT cities.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        WHERE states.name = %s
        ORDER BY cities.id ASC
    """
    cursor.execute(query, (state_name,))

    rows = cursor.fetchall()
    # join() transforme ['A', 'B', 'C'] en "A, B, C"
    print(", ".join([row[0] for row in rows]))

    cursor.close()
    db.close()


if __name__ == "__main__":
    # sys.argv[1]=user  [2]=password  [3]=database  [4]=state_name
    filter_cities_by_state(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
