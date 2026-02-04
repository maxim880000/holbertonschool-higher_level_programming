#!/usr/bin/env python3
"""
Module définissant une classe abstraite Animal et ses sous-classes Dog et Cat.
"""
from abc import ABC, abstractmethod


class Animal(ABC):
    """
    Classe abstraite représentant un animal.
    """
    @abstractmethod
    def sound(self):
        """
        Méthode abstraite devant être implémentée par les sous-classes.
        Retourne le son de l'animal.
        """
        pass


class Dog(Animal):
    """
    Classe représentant un chien.
    """
    def sound(self):
        """
        Retourne le son du chien.
        """
        return "Bark"


class Cat(Animal):
    """
    Classe représentant un chat.
    """
    def sound(self):
        """
        Retourne le son du chat.
        """
        return "Meow"
