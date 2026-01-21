#!/usr/bin/python3
# Fonction qui calcule le carré de tous les entiers d'une matrice
def square_matrix_simple(matrix=[]):
    # Crée une nouvelle matrice en utilisant une list comprehension
    # Pour chaque ligne, crée une nouvelle ligne avec les carrés
    return [[num ** 2 for num in row] for row in matrix]
