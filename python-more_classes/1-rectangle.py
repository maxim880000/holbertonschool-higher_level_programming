#!/usr/bin/python3
"""
Ce module définit une classe Rectangle.

Explication pour le man review :

- self : référence à l'objet courant
- __width / __height : attributs privés qui stockent réellement la largeur et la hauteur
- self.width / self.height : appellent les setters pour valider et stocker les valeurs
- @property : transforme une méthode en attribut en lecture seule
- @setter : permet de modifier un attribut privé avec validation
- raise : stoppe le programme si la valeur est invalide (TypeError ou ValueError)
"""

class Rectangle:
    """Classe qui représente un rectangle.
    Gère une largeur et une hauteur avec validation des valeurs.
    """

    def __init__(self, width=0, height=0):
        # Constructeur : initialise l'objet Rectangle
        # Les valeurs passent par les setters pour être validées
        self.width = width
        self.height = height

    @property
    def width(self):
        # Getter : permet de lire la largeur (__width)
        return self.__width

    @width.setter
    def width(self, value):
        # Setter : vérifie le type et la valeur avant affectation
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value  # stockage réel de la largeur

    @property
    def height(self):
        # Getter : permet de lire la hauteur (__height)
        return self.__height

    @height.setter
    def height(self, value):
        # Setter : vérifie le type et la valeur avant affectation
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value  # stockage réel de la hauteur
