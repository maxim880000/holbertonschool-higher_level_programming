# Python - Object Relational Mapping

Ce projet explore la connexion entre Python et les bases de données MySQL en utilisant deux approches :
1. **MySQLdb** : Connexion directe avec requêtes SQL
2. **SQLAlchemy** : ORM (Object-Relational Mapper) pour abstraction complète

## Objectifs d'apprentissage
- Connexion à une base de données MySQL depuis Python
- Exécution de requêtes SELECT, INSERT
- Utilisation d'un ORM
- Mappage de classes Python vers des tables MySQL
- Protection contre les injections SQL

## Configuration requise
- Python 3.8.5
- MySQLdb 2.0.x
- SQLAlchemy 1.4.x
- MySQL 8.0

## Installation
```bash
# Installer MySQLdb
sudo apt-get install python3-dev libmysqlclient-dev zlib1g-dev
sudo pip3 install mysqlclient==2.0.3

# Installer SQLAlchemy
sudo pip3 install SQLAlchemy==1.4.22
```

## Fichiers du projet
- `0-select_states.py` : Liste tous les états
- `1-filter_states.py` : Filtre les états commençant par 'N'
- `2-my_filter_states.py` : Recherche par input utilisateur (non sécurisé)
- `3-my_safe_filter_states.py` : Recherche sécurisée contre SQL injection
- `4-cities_by_state.py` : Liste toutes les villes avec leur état
- `5-filter_cities.py` : Liste les villes d'un état spécifique
- `model_state.py` : Définition du modèle State avec SQLAlchemy
- `7-model_state_fetch_all.py` : Liste tous les états via ORM
- `8-model_state_fetch_first.py` : Affiche le premier état via ORM
