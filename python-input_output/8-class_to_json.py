#!/usr/bin/python3
"""Module qui définit une fonction retournant la représentation
dictionnaire d'un objet pour la sérialisation JSON.
"""


def class_to_json(obj):
    """Retourne le dictionnaire des attributs d'un objet.

    Cette fonction récupère les attributs d'instance d'un objet
    et retourne un dictionnaire pouvant être sérialisé en JSON.
    Args:
        obj (object): Instance d'une classe.
    Returns:
        dict: Dictionnaire contenant les attributs de l'objet.
    """
    # __dict__ contient tous les attributs d'instance de l'objet
    return obj.__dict__
