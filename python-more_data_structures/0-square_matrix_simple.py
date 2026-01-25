#!/usr/bin/python3
# Fonction qui calcule le carré de tous les entiers d'une matrice
def square_matrix_simple(matrix=[]):
    # crée et retourne une nouvelle matrice où chaque élément est le 
	# carré de l’élément correspondant dans matrix
    return [[num ** 2 for num in row] for row in matrix]
