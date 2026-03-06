#!/usr/bin/python3
"""Prints the State object matching a given name using SQLAlchemy ORM."""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def get_state_by_name(username, password, database, state_name):
    """Connect to MySQL and print the id of the state matching state_name.

    Prints 'Not found' if no state matches. Safe against SQL injection
    because SQLAlchemy handles the parameterization automatically.
    """
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            username, password, database),
        pool_pre_ping=True
    )

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    # .filter() avec == génère un WHERE name = 'value' sécurisé
    state = session.query(State).filter(
        State.name == state_name
    ).first()

    if state is None:
        print("Not found")
    else:
        print(state.id)

    session.close()


if __name__ == "__main__":
    # sys.argv[1]=user  [2]=password  [3]=database  [4]=state_name
    get_state_by_name(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
