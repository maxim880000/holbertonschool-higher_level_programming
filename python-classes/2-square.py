#!/usr/bin/python3
"""Module qui définit une classe Square représentant un carré"""
# raise stop le programme en signalant un problème précis


class Square:
    """Classe qui permet de créer et manipuler un carré"""

    def __init__(self, size=0):
        """Initialise une nouvelle instance de Square
        size doit être un entier positif ou nul"""

        # Vérifie que size est bien un entier
        if not isinstance(size, int):
            raise TypeError("size must be an integer")

		# Vérifie que size est >= 0
        if size < 0:
            raise ValueError("size must be >= 0")

        # self est l'objet courant, __size est un attribut privé de cet objet
        # Il stocke la taille du carré
        self.__size = size
