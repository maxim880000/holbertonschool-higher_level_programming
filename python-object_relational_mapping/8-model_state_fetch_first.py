#!/usr/bin/python3
"""
Module pour afficher le premier état de la base de données avec SQLAlchemy.

Ce script montre comment récupérer un seul enregistrement (le premier)
au lieu de tous les enregistrements. Utilise la méthode first() de SQLAlchemy
qui est plus efficace que all() quand on ne veut qu'un seul résultat.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def fetch_first_state(username, password, database):
    """
    Affiche le premier état de la base de données.

    Utilise first() au lieu de all() pour récupérer uniquement
    le premier enregistrement. Plus efficace car SQLAlchemy ajoute
    automatiquement LIMIT 1 à la requête SQL.

    Args:
        username (str): Nom d'utilisateur MySQL
        password (str): Mot de passe MySQL
        database (str): Nom de la base de données

    Méthodes de récupération SQLAlchemy :
        .all()    : Retourne une liste de tous les objets
                    SELECT * FROM states
        
        .first()  : Retourne le premier objet ou None si vide
                    SELECT * FROM states LIMIT 1
        
        .one()    : Retourne un objet, erreur si 0 ou plusieurs résultats
                    Utilisé quand on s'attend à exactement 1 résultat
        
        .get(id)  : Retourne l'objet avec la clé primaire spécifiée
                    SELECT * FROM states WHERE id = ?

    Gestion du cas "table vide" :
        - Si la table est vide, first() retourne None
        - Il faut vérifier si state is None avant d'accéder aux attributs
        - Sinon, on obtient AttributeError: 'NoneType' object has no attribute 'id'
    """
    
    # Création du moteur de connexion à MySQL
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(username, password, database),
        pool_pre_ping=True
    )

    # Création des tables si elles n'existent pas
    Base.metadata.create_all(engine)

    # Création de la session pour interagir avec la base
    Session = sessionmaker(bind=engine)
    session = Session()

    # Requête pour récupérer le PREMIER état seulement
    # .query(State) : requête sur la table states
    # .order_by(State.id) : tri par ID croissant
    # .first() : retourne le premier résultat ou None si vide
    # 
    # SQL généré : SELECT states.id, states.name FROM states 
    #              ORDER BY states.id ASC LIMIT 1
    # 
    # Différence avec .all() :
    # - .all() charge TOUS les états en mémoire (peut être lourd)
    # - .first() charge uniquement le premier (plus rapide et économe)
    state = session.query(State).order_by(State.id).first()

    # Vérification si un état a été trouvé
    # Si la table est vide, state sera None
    if state is None:
        # Affichage du message si aucun état trouvé
        print("Nothing")
    else:
        # Affichage de l'état au format : "id: name"
        # state.id et state.name sont les attributs de l'objet State
        print("{}: {}".format(state.id, state.name))

    # Fermeture de la session pour libérer les ressources
    session.close()


if __name__ == "__main__":
    """
    Point d'entrée du script.

    Affiche le premier état ou "Nothing" si la table est vide.
    Démontre l'utilisation efficace de first() pour récupérer
    un seul enregistrement.
    """
    fetch_first_state(sys.argv[1], sys.argv[2], sys.argv[3])
