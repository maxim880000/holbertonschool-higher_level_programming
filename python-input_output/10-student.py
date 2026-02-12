#!/usr/bin/python3
"""Module qui définit une classe Student avec une méthode
permettant d'obtenir sa représentation dictionnaire,
avec possibilité de filtrer les attributs.
"""


class Student:
    """Classe représentant un étudiant avec son prénom,
    son nom et son âge.
    """

    def __init__(self, first_name, last_name, age):
        """Initialise une nouvelle instance de Student.

            first_name (str): Le prénom de l'étudiant.
            last_name (str): Le nom de famille de l'étudiant.
            age (int): L'âge de l'étudiant.
        """
        # Attributs publics
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retourne la représentation dictionnaire de l'instance.

        Si attrs est une liste de chaînes de caractères,
        seuls les attributs dont le nom est présent dans cette
        liste sont inclus dans le dictionnaire retourné.
        Sinon, tous les attributs sont retournés.

        Argument:
            attrs (list, optional): Liste des noms d'attributs à récupérer.
        Returns:
            dict: Dictionnaire des attributs sélectionnés.
        """
        # Si attrs est une liste de chaînes
        if isinstance(attrs, list) and all(isinstance(attr, str) for attr in attrs):
            # On filtre les attributs existants
            return {key: self.__dict__[key]
                    for key in attrs if key in self.__dict__}

        # Sinon on retourne tous les attributs
        return self.__dict__
