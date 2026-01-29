#!/usr/bin/python3
"""
Module qui définit une classe Square représentant un carré.

@property -> lit un attribut privé comme s'il était public
@size.setter -> modifie l'attribut privé en passant par une validation
@position.setter -> modifie l'attribut privé position avec validation
"""
# raise stop le programme en signalant un problème précis


class Square:
    """Classe qui permet de créer et manipuler un carré avec position."""

    def __init__(self, size=0, position=(0, 0)):
        """
        Initialise une nouvelle instance de Square.

        Args:
            size (int): taille du carré, doit être >= 0
            position (tuple): coordonnées horizontales et verticales (x, y)

        Raises:
            TypeError: si size n'est pas un entier ou
            position n'est pas un tuple de 2 positifs
            ValueError: si size < 0
        """
        self.size = size      # utilise le setter pour valider size
        self.position = position  # utilise le setter pour valider position

    @property
    def size(self):
        """Getter : retourne la valeur actuelle de l’attribut privé __size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter : définit la taille du carré avec validation."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value  # Attribut privé qui stocke la taille

    @property
    def position(self):
        """Getter : retourne la valeur actuelle
        de l’attribut privé __position."""
        return self.__position

    @position.setter
    def position(self, value):
        """Setter : définit la position du carré avec validation."""
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value  # Attribut privé qui stocke la position

    def area(self):
        """Méthode qui calcule et retourne l’aire du carré."""
        return self.__size * self.__size

    def my_print(self):
        """
        Méthode qui affiche le carré avec le caractère '#'.

        La position définit le décalage horizontal et vertical.
        Si size == 0, affiche une ligne vide.
        """
        if self.__size == 0:
            print()
            return

        # Décalage vertical
        for _ in range(self.__position[1]):
            print()

        # imprime le carré ligne par ligne avec décalage horizontal
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
