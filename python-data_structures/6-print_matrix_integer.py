#!/usr/bin/python3
# Fonction qui affiche une matrice d'entiers
def print_matrix_integer(matrix=[[]]):
    # Parcourt chaque ligne de la matrice
    for row in matrix:
        # Parcourt chaque élément de la ligne avec son index
        for i, num in enumerate(row):
            # Affiche l'entier avec le format {:d}
            print("{:d}".format(num), end="")
            # Ajoute un espace sauf pour le dernier élément
            if i < len(row) - 1:
                print(" ", end="")
        # Passe à la ligne suivante après chaque ligne
        print()
