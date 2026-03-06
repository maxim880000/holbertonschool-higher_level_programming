#!/usr/bin/python3
"""Lists all State objects from the database using SQLAlchemy ORM."""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def fetch_all_states(username, password, database):
    """Connect to MySQL via SQLAlchemy and print all states ordered by id."""
    # create_engine construit l'URL de connexion MySQL et prépare le pool
    # pool_pre_ping=True : vérifie la connexion avant chaque requête
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            username, password, database),
        pool_pre_ping=True
    )

    # Crée la table 'states' si elle n'existe pas encore
    Base.metadata.create_all(engine)

    # La session est le point d'entrée pour toutes les opérations ORM
    Session = sessionmaker(bind=engine)
    session = Session()

    # .query(State) → SELECT * FROM states
    # .order_by(State.id) → ORDER BY id ASC
    # .all() → retourne une liste d'objets State
    states = session.query(State).order_by(State.id).all()

    for state in states:
        print("{}: {}".format(state.id, state.name))

    session.close()


if __name__ == "__main__":
    # sys.argv[1]=user  [2]=password  [3]=database
    fetch_all_states(sys.argv[1], sys.argv[2], sys.argv[3])
