#!/usr/bin/python3
"""Module qui définit une classe Square représentant un carré
@property = permet de lire un attribut privé comme s'il était public
@size.setter = permet de modifier un attribut privé avec vérification"""


class Square:
    """Classe qui permet de créer et manipuler un carré"""

    def __init__(self, size=0):
        """
        Initialise une nouvelle instance de Square
        size doit être un entier positif ou nul
        """
        # Ici on utilise self.size pour appeler le setter
        # Cela va vérifier que la valeur est correcte avant de la stocker
        self.size = size

    @property
    def size(self):
        """Retourne la valeur actuelle de l’attribut privé __size"""
        # self.__size est l'attribut réel qui stocke la taille
        return self.__size

    @size.setter
    def size(self, value):
        """
        Définit la taille du carré avec validation
        value doit être un entier positif ou nul
        """
        # Vérifie que value est bien un entier
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        # Vérifie que value est >= 0
        if value < 0:
            raise ValueError("size must be >= 0")
        # Si tout est correct, on stocke la valeur dans l'attribut privé
        self.__size = value

    def area(self):
        """Méthode qui calcule et retourne l’aire du carré"""
        # Aire = côté * côté
        # Ici on accède directement à l'attribut privé car on est dans la classe
        return self.__size * self.__size
