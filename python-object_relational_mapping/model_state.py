#!/usr/bin/python3
"""Defines the State model mapped to the 'states' table via SQLAlchemy."""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Base est la classe parente de tous les modèles SQLAlchemy du projet
Base = declarative_base()


class State(Base):
    """State class mapped to the MySQL table 'states'.

    Chaque instance = une ligne dans la table.
    SQLAlchemy traduit automatiquement les opérations Python en SQL.
    """

    __tablename__ = 'states'  # nom de la table dans MySQL

    # Clé primaire auto-incrémentée (NOT NULL automatique avec PK)
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    # VARCHAR(128) NOT NULL
    name = Column(String(128), nullable=False)
