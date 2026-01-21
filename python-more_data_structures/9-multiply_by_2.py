#!/usr/bin/python3
# Cette ligne indique que le script doit être exécuté avec python3

def multiply_by_2(a_dictionary):
    # Cette fonction prend un dictionnaire en paramètre
    # Toutes les valeurs du dictionnaire sont des entiers

    new_dictionary = {}
    # Cette ligne crée un nouveau dictionnaire vide
    # Il servira à stocker les nouvelles valeurs multipliées par 2

    for key, value in a_dictionary.items():
        # Cette boucle parcourt le dictionnaire original
        # key correspond à la clé
        # value correspond à la valeur associée à la clé

        new_dictionary[key] = value * 2
        # Cette ligne ajoute la clé dans le nouveau dictionnaire
        # La valeur est multipliée par 2 avant d’être stockée

    return new_dictionary
    # Cette ligne retourne le nouveau dictionnaire
    # Le dictionnaire original n’est jamais modifié
