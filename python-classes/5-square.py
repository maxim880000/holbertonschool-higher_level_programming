#!/usr/bin/python3
"""Module qui définit une classe Square représentant un carré
@property = lit un attribut privé comme s'il était public
@size.setter = modifie l'attribut privé en passant par une validation"""
# raise stop le programme en signalant un problème précis


class Square:
    """Classe qui permet de créer et manipuler un carré."""

    def __init__(self, size=0):
        """
        Initialise une nouvelle instance de Square.
        size doit être un entier positif ou nul.
        """
        self.size = size  # utilise le setter pour valider et stocker __size

    @property
    def size(self):
        """Getter : retourne la valeur actuelle de l’attribut privé __size."""
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter : définit la taille du carré avec validation.
        value doit être un entier >= 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value  # Attribut privé qui stocke la taille du carré

    def area(self):
        """Méthode qui calcule et retourne l’aire du carré."""
        return self.__size * self.__size  # Aire = côté * côté

    def my_print(self):
        """
        Méthode qui affiche le carré avec le caractère '#'.

        Si la taille est 0, affiche une ligne vide.
        """
        if self.__size == 0:
            print()  # ligne vide si size = 0
            return

        # imprime le carré ligne par ligne
        for _ in range(self.__size):
            print("#" * self.__size)
