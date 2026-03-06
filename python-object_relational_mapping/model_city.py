#!/usr/bin/python3
"""Defines the City model mapped to the 'cities' table via SQLAlchemy."""

from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base


class City(Base):
    """City class mapped to the MySQL table 'cities'.

    state_id est une clé étrangère vers states.id, ce qui lie
    chaque ville à un état via la relation entre les deux tables.
    """

    __tablename__ = 'cities'  # nom de la table dans MySQL

    # Clé primaire auto-incrémentée
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    # VARCHAR(128) NOT NULL
    name = Column(String(128), nullable=False)
    # Clé étrangère : cities.state_id référence states.id
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
