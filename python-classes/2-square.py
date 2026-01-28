#!/usr/bin/python3
"""Module qui définit une classe Square représentant un carré"""


class Square:
    """Classe qui permet de créer et manipuler un carré"""

    def __init__(self, size=0):
        """Initialise un nouvel objet Square"""
        """size représente la longueur d’un côté du carré
        Il doit obligatoirement être un entier positif ou nul"""

        # Vérifie que size est bien un entier
        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        # Vérifie que size n'est pas négatif
        if size < 0:
            raise ValueError("size must be >= 0")

        # Attribut privé qui stocke la taille du carré
        self.__size = size
