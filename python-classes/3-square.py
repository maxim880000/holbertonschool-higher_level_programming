#!/usr/bin/python3


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

        # self est l'objet courant, __size est un attribut privé de cet objet
        # Il stocke la taille du carré
        self.__size = size

    def area(self):
        """Méthode qui calcule et retourne l’aire du carré
        prends l’attribut de l’objet courant"""
        return self.__size * self.__size
        """Aire = côté * côté"""
