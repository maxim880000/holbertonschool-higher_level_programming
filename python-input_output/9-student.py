#!/usr/bin/python3
"""Module qui définit une classe Student avec une méthode
permettant d'obtenir sa représentation dictionnaire.
"""


class Student:
    """Classe représentant un étudiant avec son prénom,
    son nom et son âge.
    """

    def __init__(self, first_name, last_name, age):
        """Initialise une nouvelle instance de Student.

        Argumetn:
            first_name (str): Le prénom de l'étudiant.
            last_name (str): Le nom de famille de l'étudiant.
            age (int): L'âge de l'étudiant.
        """
        # Attributs publics de l'instance
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retourne la représentation dictionnaire de l'instance.
        Cette méthode récupère les attributs de l'étudiant
        sous forme de dictionnaire afin de permettre
        une sérialisation JSON.

        Returns:
            dict: Dictionnaire contenant les attributs de l'étudiant.
        """
        # __dict__ contient tous les attributs d'instance
        return self.__dict__
