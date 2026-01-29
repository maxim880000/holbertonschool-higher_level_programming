#!/usr/bin/python3
"""Module qui définit une classe Square représentant un carré"""
"""raise stop le programme en signalant un problème précis"""


class Square:
    """class qui permet de creer et manipuler un carré"""

    def __init__(self, size=0):
        """
        Initialise une nouvelle instance de Square
        size doit être un entier positif ou nul
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >=0")

        """Attribut privé qui stocke la taille du carré"""
        self.__size = size

    def area(self):
        """Méthode qui calcule et retourne l’aire du carré"""
        return self.__size * self.__size
        """Aire = côté * côté"""
