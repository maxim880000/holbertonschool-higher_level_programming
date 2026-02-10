#!/usr/bin/python3
"""
Définit une classe Rectangle avec largeur et hauteur privées
self représente l'objet courant
@property permet de lire un attribut privé comme s'il était public
@<attr>.setter permet de modifier un attribut privé avec contrôle
__width, __height attributs privés, accessibles via getter/setter
__str__ affiche le rectangle avec #
__repr__ permet de recréer l'objet avec eval()
"""

class Rectangle:
    """Représente un rectangle avec largeur et hauteur"""

    def __init__(self, width=0, height=0):
        """Initialise le rectangle avec une largeur et une hauteur"""
        # Utilise les setters pour valider et stocker les valeurs
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter : retourne la largeur"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter : définit la largeur avec validation"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")  # stop si type incorrect
        if value < 0:
            raise ValueError("width must be >= 0")       # stop si valeur négative
        self.__width = value  # stockage réel de la largeur

    @property
    def height(self):
        """Getter : retourne la hauteur"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter : définit la hauteur avec validation"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")  # stop si type incorrect
        if value < 0:
            raise ValueError("height must be >= 0")       # stop si valeur négative
        self.__height = value  # stockage réel de la hauteur

    def area(self):
        """Retourne l'aire du rectangle"""
        return self.__width * self.__height  # largeur * hauteur

    def perimeter(self):
        """Retourne le périmètre du rectangle, 0 si largeur ou hauteur = 0"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)  # périmètre = 2*(L+H)

    def __str__(self):
        """Affiche le rectangle avec le caractère #"""
        if self.__width == 0 or self.__height == 0:
            return ""  # retourne chaîne vide si rectangle vide
        # retourne le rectangle ligne par ligne
        return "\n".join(["#" * self.__width for _ in range(self.__height)])

    def __repr__(self):
        """Retourne une représentation du rectangle utilisable avec eval()"""
        return f"Rectangle({self.__width}, {self.__height})"  # format pour recréer l'objet
