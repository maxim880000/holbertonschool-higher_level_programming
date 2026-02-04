#!/usr/bin/python3
"""Defines a base geometry class with validation methods."""


class BaseGeometry:
    """class pour la géométrie"""
    def area(self):
        """Lève une exception car non implémentée"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Valide qu'une valeur est un entier positif mais pas un 
        booléen(car bool hérite de int en Python)"""
        if not isinstance(value, int) or isinstance(value, bool):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
