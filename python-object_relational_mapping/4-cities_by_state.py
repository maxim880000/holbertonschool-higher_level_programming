#!/usr/bin/python3
"""Lists all cities with their state name using a SQL JOIN."""

import MySQLdb
import sys


def list_cities_by_state(username, password, database):
    """Connect to MySQL and print all cities with state, ordered by id."""
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database,
        charset="utf8"
    )

    cursor = db.cursor()
    # JOIN lie cities à states via cities.state_id = states.id
    query = """
        SELECT cities.id, cities.name, states.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        ORDER BY cities.id ASC
    """
    cursor.execute(query)

    rows = cursor.fetchall()  # chaque ligne : (city_id, city_name, state_name)
    for row in rows:
        print(row)

    cursor.close()
    db.close()


if __name__ == "__main__":
    # sys.argv[1]=user  [2]=password  [3]=database
    list_cities_by_state(sys.argv[1], sys.argv[2], sys.argv[3])
