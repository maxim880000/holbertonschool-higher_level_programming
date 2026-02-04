#!/usr/bin/python3
"""
Module qui définit la classe Square héritant
de Rectangle avec affichage spécifique.
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Classe Square qui hérite de Rectangle.
    Permet de représenter un carré avec une
    taille donnée et un affichage spécifique.
    """
    def __init__(self, size):
        """
        Initialise un carré avec une taille validée.
        Args:
            size (int): taille du carré (doit être > 0)
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """
        Calcule et retourne l'aire du carré.
        Returns:
            int: aire du carré
        """
        return self.__size ** 2

    def __str__(self):
        """
        Retourne la représentation en chaîne du carré.
        Returns:
            str: description du carré
        """
        return "[Square] {}/{}".format(self.__size, self.__size)
