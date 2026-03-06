#!/usr/bin/python3
"""Deletes all State objects whose name contains 'a' using SQLAlchemy ORM."""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def delete_states_with_a(username, password, database):
    """Connect to MySQL and delete all states whose name contains 'a'."""
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            username, password, database),
        pool_pre_ping=True
    )

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    # Récupère tous les states contenant 'a' puis les supprime un par un
    states = session.query(State).filter(
        State.name.like('%a%')
    ).all()

    for state in states:
        session.delete(state)  # marque l'objet → DELETE SQL

    session.commit()  # exécute tous les DELETE en une transaction

    session.close()


if __name__ == "__main__":
    # sys.argv[1]=user  [2]=password  [3]=database
    delete_states_with_a(sys.argv[1], sys.argv[2], sys.argv[3])
