#!/usr/bin/env python3
"""
Module définissant une classe abstraite Animal et ses sous-classes Dog et Cat.
"""
# On importe ABC et abstractmethod pour créer une classe abstraite
from abc import ABC, abstractmethod

# Définition de la classe abstraite Animal
class Animal(ABC):
    """
    Classe abstraite représentant un animal.
    """
    @abstractmethod
    def sound(self):
        """
        Méthode abstraite : chaque animal doit définir son propre son.
        """
        pass  # Pas d'implémentation ici, à faire dans les sous-classes

# Classe Dog qui hérite de Animal
class Dog(Animal):
    """
    Classe représentant un chien.
    """
    def sound(self):
        """
        Retourne le son du chien.
        """
        return "Bark"  # Le chien aboie

# Classe Cat qui hérite de Animal
class Cat(Animal):
    """
    Classe représentant un chat.
    """
    def sound(self):
        """
        Retourne le son du chat.
        """
        return "Meow"  # Le chat miaule
