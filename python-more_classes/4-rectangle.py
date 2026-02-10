#!/usr/bin/python3
"""
Module définissant la classe Rectangle.

CONCEPTS CLÉS :
- @property : transforme une méthode en attribut lisible (rect.width au lieu de rect.width())
- @width.setter : permet de modifier l'attribut avec validation (rect.width = 5)
- __repr__() : retourne une chaîne pour recréer l'objet avec eval() (ex: "Rectangle(5, 3)")
- __str__() : retourne une chaîne lisible pour print() (ex: affiche le rectangle en #)
- .join() : assemble une liste en chaîne (ex: "\n".join(["##", "##"]) → "##\n##")
"""


class Rectangle:
    """
    Classe représentant un rectangle avec largeur et hauteur.
    
    Attributes:
        __width (int): Largeur privée du rectangle.
        __height (int): Hauteur privée du rectangle.
    """

    def __init__(self, width=0, height=0):
        """
        Initialise un nouveau rectangle.

        Args:
            width (int): Largeur du rectangle. Par défaut 0.
            height (int): Hauteur du rectangle. Par défaut 0.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Récupère la largeur du rectangle.

        Returns:
            int: La largeur actuelle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Définit la largeur avec validation.

        Args:
            value (int): Nouvelle largeur (doit être >= 0).

        Raises:
            TypeError: Si value n'est pas un entier.
            ValueError: Si value est négatif.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Récupère la hauteur du rectangle.

        Returns:
            int: La hauteur actuelle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Définit la hauteur avec validation.

        Args:
            value (int): Nouvelle hauteur (doit être >= 0).

        Raises:
            TypeError: Si value n'est pas un entier.
            ValueError: Si value est négatif.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Calcule l'aire du rectangle.

        Returns:
            int: L'aire (largeur × hauteur).
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Calcule le périmètre du rectangle.

        Returns:
            int: Le périmètre, ou 0 si largeur ou hauteur = 0.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """
        Représente le rectangle avec des caractères #.

        Returns:
            str: Représentation visuelle du rectangle.
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        return "\n".join(["#" * self.__width for _ in range(self.__height)])

    def __repr__(self):
        """
        Retourne une représentation du rectangle pour eval().

        Returns:
            str: Format "Rectangle(width, height)".
        """
        return f"Rectangle({self.__width}, {self.__height})"