#!/usr/bin/python3
"""valeur usr tape pour creation du carré = size"""
# self représente l'objet en cours de création


class Square:
    """class qui represente un carré"""
    def __init__(self, size):
        """__init__ constructeur (creer un objet ini ses attributs)"""
        self.__size = size
        """self.__size devient un attribut de l’objet (privé)"""
        """size est stocké dasn l'insatance de square"""
