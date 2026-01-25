#!/usr/bin/python3

# Fonction qui affiche une chaîne en majuscules
def uppercase(str):
    # Parcours chaque caractère de la chaîne
    for c in str:
        # Si le caractère est une lettre minuscule ('a' à 'z')
        if ord(c) >= 97 and ord(c) <= 122:
            # Convertit la minuscule en majuscule en utilisant ASCII
            c = chr(ord(c) - 32)
        # Affiche le caractère (majuscules ou non)
        print("{}".format(c), end="")
    # affiche un saut de ligne
    print()
