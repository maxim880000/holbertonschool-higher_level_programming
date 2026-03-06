#!/usr/bin/python3
"""Prints all City objects from the database with their state."""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City


def fetch_cities_by_state(username, password, database):
    """Connect to MySQL and print all cities with state name, ordered by id."""
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            username, password, database),
        pool_pre_ping=True
    )

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    # JOIN ORM : City.state_id == State.id lie les deux tables
    # Équivalent SQL : JOIN states ON cities.state_id = states.id
    results = session.query(City, State).filter(
        City.state_id == State.id
    ).order_by(City.id).all()

    for city, state in results:
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    session.close()


if __name__ == "__main__":
    # sys.argv[1]=user  [2]=password  [3]=database
    fetch_cities_by_state(sys.argv[1], sys.argv[2], sys.argv[3])
