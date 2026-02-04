#!/usr/bin/python3
"""
Module qui définit la classe Rectangle héritant de BaseGeometry.
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """
    Classe Rectangle qui hérite de BaseGeometry.
    Permet de représenter un rectangle avec une largeur et une hauteur.
    """
    def __init__(self, width, height):
        """
        Initialise un rectangle avec largeur et hauteur validées.
        Args:
            width (int): largeur du rectangle (doit être > 0)
            height (int): hauteur du rectangle (doit être > 0)
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        Calcule et retourne l'aire du rectangle.
        Returns:
            int: aire du rectangle
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Retourne la représentation en chaîne du rectangle.
        Returns:
            str: description du rectangle
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
