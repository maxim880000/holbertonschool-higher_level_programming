#!/usr/bin/python3
"""objet qu'on creer = self"""
"""valeur usr tape pour creation du carré = size"""


class Square:
    """class qui represente un carré"""
    def __init__(self, size):
        """__init__ constructeur (creer un objet ini ses attributs)"""
        self.__size = size
        """creer un attribut privé (__) __size"""
