#!/usr/bin/python3

# Fonction qui affiche une chaîne en majuscules suivie d'un saut de ligne
def uppercase(str):

    # On parcourt chaque caractère de la chaîne
    for c in str:
        # Si le caractère est une lettre minuscule ('a' à 'z')
        if ord(c) >= 97 and ord(c) <= 122:
            # On affiche le caractère converti en majuscule
            # chr(ord(c) - 32) transforme 'a'-'z' en 'A'-'Z'
            print("{}".format(chr(ord(c) - 32)), end="")
        else:
            # Si ce n'est pas une minuscule, on l'affiche tel quel
            print("{}".format(c), end="")
    # Après avoir affiché toute la chaîne, on saute une ligne
    print()
