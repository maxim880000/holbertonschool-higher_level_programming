#!/usr/bin/python3

def multiply_by_2(a_dictionary):
# Toutes les valeurs du dictionnaire sont des entiers

    new_dictionary = {}
    # Cette ligne crée un nouveau dictionnaire vide

    for key, value in a_dictionary.items():
    # parcourt toutes les paires clé-valeur du dictionnaire,
	# en donnant à chaque tour key la clé et
	# value la valeur correspondante.

        new_dictionary[key] = value * 2
        # Cette ligne ajoute la clé dans le nouveau dictionnaire
        # La valeur est multipliée par 2 avant d’être stockée

    return new_dictionary
