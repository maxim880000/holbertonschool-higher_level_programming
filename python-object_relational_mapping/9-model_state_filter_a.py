#!/usr/bin/python3
"""Lists all State objects containing the letter 'a' using SQLAlchemy ORM."""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def filter_states_with_a(username, password, database):
    """Connect to MySQL and print states whose name contains 'a'."""
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            username, password, database),
        pool_pre_ping=True
    )

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    # .filter() → WHERE en SQL  |  State.name.like('%a%') → LIKE '%a%'
    states = session.query(State).filter(
        State.name.like('%a%')
    ).order_by(State.id).all()

    for state in states:
        print("{}: {}".format(state.id, state.name))

    session.close()


if __name__ == "__main__":
    # sys.argv[1]=user  [2]=password  [3]=database
    filter_states_with_a(sys.argv[1], sys.argv[2], sys.argv[3])
