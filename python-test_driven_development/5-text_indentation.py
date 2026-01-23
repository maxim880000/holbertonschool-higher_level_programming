#!/usr/bin/python3
"""
Module qui fournit une fonction pour afficher un texte
avec deux sauts de ligne après chaque '.', '?' ou ':'.
"""


def text_indentation(text):
    """
    Affiche le texte avec 2 lignes vides après '.', '?' et ':'.
    """

    # Vérifie que text est une chaîne
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # Initialise la position de lecture
    start = 0

    # Boucle sur le texte
    for i in range(len(text)):
        if text[i] in ".?:":
            # Affiche la portion de texte et supprime espaces début/fin
            print(text[start:i + 1].strip())
            print()  # deuxième ligne vide
            start = i + 1  # nouvelle portion commence après le caractère
    # Affiche le reste du texte si nécessaire
    if start < len(text):
        print(text[start:].strip())
