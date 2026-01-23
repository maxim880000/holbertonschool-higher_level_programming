#!/usr/bin/python3
"""
This module provides a function that prints a square using the # character.

The square size is defined by an integer value.
"""


def print_square(size):
    """
    Print a square of a given size using the # character.
    """

    # Vérifie que size est un entier
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    # Vérifie que size n'est pas négatif
    if size < 0:
        raise ValueError("size must be >= 0")

    # Boucle sur la hauteur du carré
    for i in range(size):
        # Affiche une ligne de # de longueur size
        print("#" * size)
