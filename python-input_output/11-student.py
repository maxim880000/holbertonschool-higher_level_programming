#!/usr/bin/python3
"""Module qui définit la classe Student.

Cette classe permet de représenter un étudiant avec ses attributs publics
et fournit des méthodes pour :
- obtenir la représentation dictionnaire de l'objet (sérialisation),
- recharger/modifier l'objet à partir d'un dictionnaire (désérialisation).
"""


class Student:
    """Classe représentant un étudiant.

    Attributs publics :
        first_name (str): prénom de l'étudiant
        last_name (str): nom de famille de l'étudiant
        age (int): âge de l'étudiant
    """

    def __init__(self, first_name, last_name, age):
        """Initialise un nouvel étudiant.

        Args:
            first_name (str): prénom de l'étudiant
            last_name (str): nom de famille de l'étudiant
            age (int): âge de l'étudiant
        """
        # On crée les attributs publics de l'instance
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retourne la représentation dictionnaire de l'étudiant.

        Si 'attrs' est une liste de chaînes de caractères, seuls
        les attributs correspondants sont inclus dans le dictionnaire.
        Sinon, tous les attributs de l'objet sont retournés.

        Args:
            attrs (list, optional): liste des noms d'attributs à inclure

        Returns:
            dict: dictionnaire des attributs sélectionnés
        """
        # Vérifie que attrs est bien une liste de chaînes
        if isinstance(attrs, list) and all(isinstance(attr, str) for attr in attrs):
            # On ne prend que les attributs existants dans __dict__ et présents dans attrs
            return {key: self.__dict__[key] for key in attrs if key in self.__dict__}

        # Si aucun filtre n'est fourni, on retourne tous les attributs
        return self.__dict__

    def reload_from_json(self, json):
        """Remplace les attributs de l'étudiant avec ceux d'un dictionnaire.

        Les clés du dictionnaire correspondent aux noms des attributs
        et les valeurs aux valeurs à assigner.

        Args:
            json (dict): dictionnaire contenant les attributs à mettre à jour
        """
        # On parcourt chaque clé/valeur du dictionnaire et on met à jour l'objet
        for key, value in json.items():
            setattr(self, key, value)  # équivalent à self.key = value
