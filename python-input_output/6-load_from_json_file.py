#!/usr/bin/python3
"""Module qui définit une fonction pour créer un objet Python
à partir du contenu d'un fichier JSON.
"""

import json


def load_from_json_file(filename):
    """Crée un objet Python à partir d'un fichier JSON.

    Cette fonction ouvre un fichier, lit son contenu JSON
    et retourne l'objet Python correspondant.
    Args:
        filename (str): Le nom du fichier à lire.
    Returns:
        object: L'objet Python représenté par le fichier JSON.
    """
    # Ouverture du fichier en mode lecture
    # Le mot-clé "with" garantit que le fichier sera fermé automatiquement
    with open(filename, 'r', encoding='utf-8') as file:
        # json.load() lit directement le fichier
        # et convertit le JSON en structure Python
        return json.load(file)
