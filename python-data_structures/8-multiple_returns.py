#!/usr/bin/python3
# Fonction qui retourne un tuple avec la longueur et le premier caractère
def multiple_returns(sentence):
    # Calcule la longueur de la chaîne
    length = len(sentence)
    # Récupère le premier caractère, ou None si la chaîne est vide
    first = sentence[0] if length > 0 else None
    # Retourne un tuple avec la longueur et le premier caractère
    return (length, first)
