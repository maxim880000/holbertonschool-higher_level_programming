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
        # Utilise le setter pour valider la valeur et stocker __size
        self.size = size

    @property
    def size(self):
        """Getter : retourne la valeur actuelle de l’attribut privé __size."""
        return self.__size  # retourne la valeur stockée dans l'attribut privé

    @size.setter
    def size(self, value):
        """
        Setter : définit la taille du carré avec validation.
        value doit être un entier >= 0.
        """
        # Vérifie que value est bien un entier
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        # Vérifie que value est >= 0
        if value < 0:
            raise ValueError("size must be >= 0")
        # Stocke la valeur validée dans l'attribut privé
        self.__size = value

    def area(self):
        """Méthode qui calcule et retourne l’aire du carré."""
        # Aire = côté * côté
        # On utilise directement l'attribut privé car on est dans la classe
        return self.__size * self.__size

    def my_print(self):
        """
        Méthode qui affiche le carré avec le caractère '#'.
        Si la taille est 0, affiche une ligne vide.
        """
        # Cas où le carré est vide
        if self.__size == 0:
            print()  # affiche une ligne vide
            return

        # Imprime le carré ligne par ligne
        # Chaque ligne contient __size caractères '#'
        for _ in range(self.__size):
            print("#" * self.__size)
