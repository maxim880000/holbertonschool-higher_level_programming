#!/usr/bin/python3
"""
Module définissant la classe Rectangle.

CONCEPTS CLÉS :
- @property : transforme une méthode en attribut lisible
- @width.setter : permet de modifier l'attribut avec validation
- __repr__() : retourne une chaîne pour recréer l'objet avec eval()
- __str__() : retourne une chaîne lisible pour print()
- __del__() : appelée automatiquement lors de la suppression de l'objet
- @staticmethod : méthode qui appartient à la classe sans modifier classe/instance
- .join() : assemble une liste en chaîne
"""


class Rectangle:
    """
    Classe représentant un rectangle avec largeur et hauteur.
    
    Attributes:
        number_of_instances (int): Compte le nombre d'instances créées.
        print_symbol (str): Symbole pour dessiner le rectangle.
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialise un nouveau rectangle."""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Récupère la largeur."""
        return self.__width

    @width.setter
    def width(self, value):
        """Définit la largeur avec validation."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Récupère la hauteur."""
        return self.__height

    @height.setter
    def height(self, value):
        """Définit la hauteur avec validation."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calcule l'aire (largeur × hauteur)."""
        return self.__width * self.__height

    def perimeter(self):
        """Calcule le périmètre, ou 0 si largeur ou hauteur = 0."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Représente le rectangle avec print_symbol."""
        if self.__width == 0 or self.__height == 0:
            return ""
        symbol = str(self.print_symbol)
        return "\n".join([
            symbol * self.__width
            for _ in range(self.__height)
        ])

    def __repr__(self):
        """Retourne une représentation pour eval()."""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Destructeur : décrémente le compteur et affiche un message."""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Retourne le rectangle avec la plus grande aire.

        Args:
            rect_1 (Rectangle): Premier rectangle.
            rect_2 (Rectangle): Deuxième rectangle.

        Returns:
            Rectangle: Le rectangle avec la plus grande aire.

        Raises:
            TypeError: Si rect_1 ou rect_2 n'est pas un Rectangle.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2