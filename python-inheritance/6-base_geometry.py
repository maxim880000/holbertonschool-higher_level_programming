#!/usr/bin/python3
"""Defines a base geometry class."""


class BaseGeometry:
    """class BaseGeometry"""
    def area(self):
        """raises an Exception with the
        message area() is not implemented (fait rien)"""
        # lancer une erreur dans le programme il s'arrete
        raise Exception("area() is not implemented")
        # cette fonction doit être codée avant de pouvoir être utilisée
