#!/usr/bin/python3
# Fonction qui supprime tous les caractères 'c' et 'C' d'une chaîne
def no_c(my_string):
    # Crée une nouvelle chaîne vide pour stocker le résultat
    new_string = ""
    # Parcourt chaque caractère de la chaîne originale
    for char in my_string:
        # Vérifie si le caractère n'est pas 'c' ou 'C'
        if char != 'c' and char != 'C':
            # Ajoute le caractère à la nouvelle chaîne
            new_string += char
    # Retourne la nouvelle chaîne sans 'c' et 'C'
    return new_string
