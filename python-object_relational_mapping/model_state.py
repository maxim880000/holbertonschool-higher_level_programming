#!/usr/bin/python3
"""
Module de définition du modèle State pour SQLAlchemy.

Ce fichier définit la classe State qui représente la table 'states'
dans la base de données. SQLAlchemy (ORM) fait le lien entre cette
classe Python et la table MySQL, permettant de manipuler les données
comme des objets Python au lieu d'écrire du SQL.
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Création de la classe de base pour tous les modèles
# declarative_base() retourne une classe de base dont hériteront
# tous nos modèles. Cette base contient les métadonnées nécessaires
# pour mapper les classes Python aux tables SQL.
Base = declarative_base()


class State(Base):
    """
    Classe représentant un état dans la base de données.

    Cette classe hérite de Base (fournie par declarative_base).
    SQLAlchemy utilise les attributs de classe pour créer et gérer
    la table MySQL correspondante.

    Attributs de classe :
        __tablename__ (str): Nom de la table MySQL ('states')
        id (Column): Clé primaire auto-incrémentée
        name (Column): Nom de l'état (chaîne de 128 caractères max)

    Fonctionnement de l'ORM :
        Classe Python         ←→  Table MySQL
        ─────────────────────────────────────
        State                 ←→  states
        state.id              ←→  states.id
        state.name            ←→  states.name
        
        Opérations Python     ←→  Requêtes SQL
        ─────────────────────────────────────
        State()               ←→  INSERT INTO states
        session.query(State)  ←→  SELECT * FROM states
        state.name = "Texas"  ←→  UPDATE states SET name = "Texas"
        session.delete(state) ←→  DELETE FROM states

    Avantages de l'ORM :
        - Plus de requêtes SQL à écrire manuellement
        - Code plus pythonique et orienté objet
        - Protection automatique contre les injections SQL
        - Changement de base de données facilité (MySQL → PostgreSQL, etc.)
    """
    
    # Nom de la table dans la base de données
    # SQLAlchemy crée ou utilise une table nommée 'states'
    __tablename__ = 'states'

    # Définition de la colonne 'id'
    # Column() définit une colonne dans la table
    # Integer : type de données (INT en MySQL)
    # primary_key=True : cette colonne est la clé primaire
    # autoincrement=True : MySQL incrémente automatiquement la valeur
    # nullable=False : la valeur ne peut pas être NULL
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)

    # Définition de la colonne 'name'
    # String(128) : type VARCHAR(128) en MySQL
    # nullable=False : le nom ne peut pas être NULL (obligatoire)
    name = Column(String(128), nullable=False)

    # Note : Pas besoin de définir __init__, __repr__, etc.
    # SQLAlchemy génère automatiquement ces méthodes.
    # On peut les ajouter si on veut personnaliser le comportement.
