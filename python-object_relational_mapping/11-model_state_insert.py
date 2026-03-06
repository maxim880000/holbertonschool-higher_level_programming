#!/usr/bin/python3
"""Adds the State 'Louisiana' to the database using SQLAlchemy ORM."""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def insert_state(username, password, database):
    """Connect to MySQL, insert 'Louisiana', and print its new id."""
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            username, password, database),
        pool_pre_ping=True
    )

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    # Création d'un nouvel objet State (équivalent INSERT INTO states)
    new_state = State(name="Louisiana")
    session.add(new_state)   # ajoute l'objet à la session
    session.commit()         # exécute le INSERT et génère l'id auto-incrémenté

    print(new_state.id)  # l'id est disponible après le commit

    session.close()


if __name__ == "__main__":
    # sys.argv[1]=user  [2]=password  [3]=database
    insert_state(sys.argv[1], sys.argv[2], sys.argv[3])
