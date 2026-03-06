#!/usr/bin/python3
"""
Module pour lister tous les états en utilisant SQLAlchemy ORM.

Ce script démontre l'utilisation de SQLAlchemy comme ORM (Object-Relational Mapper).
Au lieu d'écrire du SQL brut, on manipule des objets Python qui représentent
les lignes de la table. SQLAlchemy traduit automatiquement ces opérations en SQL.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def fetch_all_states(username, password, database):
    """
    Liste tous les états en utilisant SQLAlchemy ORM.

    Cette fonction montre la différence fondamentale avec MySQLdb :
    - MySQLdb : écriture de requêtes SQL manuelles
    - SQLAlchemy : manipulation d'objets Python

    Args:
        username (str): Nom d'utilisateur MySQL
        password (str): Mot de passe MySQL
        database (str): Nom de la base de données

    Étapes du processus ORM :
        1. Créer un moteur (engine) : connexion à la base de données
        2. Créer une session : gestionnaire de transactions
        3. Requêter avec query() : récupération d'objets State
        4. Itérer sur les objets : accès direct aux attributs
        5. Fermer la session : libération des ressources

    Comparaison SQL vs ORM :
        SQL brut (MySQLdb) :
            cursor.execute("SELECT * FROM states ORDER BY id ASC")
            rows = cursor.fetchall()
            for row in rows:
                print(row)
        
        ORM (SQLAlchemy) :
            states = session.query(State).order_by(State.id).all()
            for state in states:
                print(f"{state.id}: {state.name}")
        
        Avantages de l'ORM :
        - Code plus lisible et pythonique
        - Protection automatique contre injections SQL
        - Objets avec attributs (state.id, state.name) au lieu de tuples
        - Changement de DB facilité (MySQL → PostgreSQL sans réécrire le code)
    """
    
    # 1. Création du moteur de base de données (engine)
    # create_engine() crée une connexion à MySQL
    # Format : 'mysql+mysqldb://user:password@host/database'
    # pool_pre_ping=True : vérifie que la connexion est active avant chaque requête
    # Cela évite les erreurs si la connexion MySQL expire
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(username, password, database),
        pool_pre_ping=True
    )

    # 2. Création de toutes les tables définies dans Base
    # Base.metadata contient les informations sur toutes les classes héritant de Base
    # create_all() crée les tables si elles n'existent pas déjà
    # Dans notre cas, cela crée la table 'states' si elle n'existe pas
    Base.metadata.create_all(engine)

    # 3. Création d'une fabrique de sessions
    # sessionmaker() crée une classe Session configurée pour notre engine
    # bind=engine : lie la session à notre connexion MySQL
    Session = sessionmaker(bind=engine)

    # 4. Création d'une instance de session
    # La session gère les transactions et les requêtes
    # C'est l'équivalent du curseur dans MySQLdb, mais en plus puissant
    session = Session()

    # 5. Requête pour récupérer tous les états
    # session.query(State) : créé une requête sur la classe State
    # .order_by(State.id) : trie par colonne id (comme ORDER BY id en SQL)
    # .all() : exécute la requête et retourne tous les résultats
    # 
    # SQLAlchemy génère automatiquement cette requête SQL :
    # SELECT states.id, states.name FROM states ORDER BY states.id ASC
    states = session.query(State).order_by(State.id).all()

    # 6. Affichage de chaque état
    # 'states' est une liste d'objets State
    # Chaque 'state' a les attributs 'id' et 'name' définis dans model_state.py
    # On peut accéder directement à ces attributs au lieu de manipuler des tuples
    for state in states:
        print("{}: {}".format(state.id, state.name))

    # 7. Fermeture de la session
    # Libère les ressources et ferme la connexion
    session.close()


if __name__ == "__main__":
    """
    Point d'entrée du script.

    Démontre l'utilisation de SQLAlchemy ORM pour récupérer
    et afficher des données sans écrire de SQL manuel.
    """
    fetch_all_states(sys.argv[1], sys.argv[2], sys.argv[3])
