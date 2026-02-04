#!/usr/bin/python3
"""
Module qui définit la classe Square héritant de Rectangle.
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Classe Square qui hérite de Rectangle.
    Permet de représenter un carré avec une taille donnée.
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
