#!/usr/bin/python3
"""Module qui définit une classe Square représentant un carré
@property = lit un attribut privé comme s'il était public
@size.setter = modifie l'attribut privé en passant par une validation"""
# raise stop le programme en signalant un problème précis


class Square:
    """Classe qui permet de créer et manipuler un carré"""

    def __init__(self, size=0):
        """
        Initialise une nouvelle instance de Square
        size doit être un entier positif ou nul
        """
        self.size = size  # définis la taille de l’objet pass by validation

    @property
    def size(self):
        """Retourne la valeur actuelle de l’attribut privé __size"""
        return self.__size

    @size.setter
    def size(self, value):
        """
        Définit la taille du carré avec validation
        value doit être un entier positif ou nul
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value  # Attribut privé qui stocke la taille du carré

    def area(self):
        """Méthode qui calcule et retourne l’aire du carré"""
        return self.__size * self.__size  # Aire = côté * côté
