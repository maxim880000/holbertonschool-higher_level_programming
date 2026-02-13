#!/usr/bin/env python3
"""Module qui fournit des fonctions pour sérialiser et
désérialiser un dictionnaire Python en JSON.
"""

# On importe le module 'json' pour pouvoir convertir des objets Python
# (dictionnaires, listes, etc.) en format JSON et vice versa.
import json


def serialize_and_save_to_file(data, filename):
    """Sérialise un dictionnaire Python et l'enregistre dans un fichier JSON.

    Args:
        data (dict): Dictionnaire Python à sérialiser.
        filename (str): Nom du fichier de sortie.
    """
    # Ouverture du fichier en mode écriture ('w') avec encodage UTF-8.
    # Si le fichier existe déjà, il sera remplacé.
    with open(filename, 'w', encoding='utf-8') as f:
        # json.dump() convertit le dictionnaire en JSON et écrit directement dans le fichier
        json.dump(data, f)


def load_and_deserialize(filename):
    """Charge un fichier JSON et retourne le dictionnaire Python correspondant.

    Args:
        filename (str): Nom du fichier à lire.

    Returns:
        dict: Dictionnaire Python désérialisé depuis le fichier JSON.
    """
    # Ouverture du fichier en mode lecture ('r') avec encodage UTF-8
    with open(filename, 'r', encoding='utf-8') as f:
        # json.load() lit le contenu JSON du fichier et le convertit en dictionnaire Python
        return json.load(f)
