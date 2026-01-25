#!/usr/bin/python3

# (0 à 9)
for i in range(10):
    # Pour chaque premier chiffre i
    for j in range(i + 1, 10):
        # Si ce n’est pas la dernière combinaison 89
        # on affiche les deux chiffres suivis de ", "
        if i != 8 or j != 9:
            print("{}{}".format(i, j), end=", ")
        # Si c’est la dernière combinaison "89"
        # on affiche les deux chiffres suivis d’un saut de ligne
        else:
            print("{}{}".format(i, j))
