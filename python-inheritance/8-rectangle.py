#!/usr/bin/python3
"""Module defining Rectangle class"""
"""mettre h et w en privé et checker si c'est des int"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """classe rectangle qui herite de BaseGeometry"""
    def __init__(self, width, height):
        """méthode qui est appelée quand tu crées un nouvel objet
        initialise t valeur de depart"""

        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
