#!/usr/bin/python3
# Fonction qui affiche un dictionnaire avec les clés triées
def print_sorted_dictionary(a_dictionary):
    # Parcourt le dictionnaire avec les clés triées alphabétiquement
    for key in sorted(a_dictionary.keys()):
        # Affiche chaque clé et sa valeur
        print("{}: {}".format(key, a_dictionary[key]))
