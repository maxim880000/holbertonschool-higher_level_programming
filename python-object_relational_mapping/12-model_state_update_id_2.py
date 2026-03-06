#!/usr/bin/python3
"""Changes the name of the State with id=2 to 'New Mexico' using SQLAlchemy."""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def update_state(username, password, database):
    """Connect to MySQL and rename the state with id=2 to 'New Mexico'."""
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            username, password, database),
        pool_pre_ping=True
    )

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    # Récupère l'objet State avec id=2 (None si inexistant)
    state = session.query(State).filter(State.id == 2).first()

    if state is not None:
        state.name = "New Mexico"  # modification de l'attribut → UPDATE en SQL
        session.commit()           # envoie le UPDATE à la base

    session.close()


if __name__ == "__main__":
    # sys.argv[1]=user  [2]=password  [3]=database
    update_state(sys.argv[1], sys.argv[2], sys.argv[3])
