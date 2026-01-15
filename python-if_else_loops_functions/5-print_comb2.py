#!/usr/bin/python3

for i in range(100):  # Boucle de 0 à 99 inclus
    if i != 99:  # Tous les nombres sauf le dernier
        # {:02d} force 2 chiffres avec un zéro devant
        print("{:02d}, ".format(i), end="")
    else:
        print("{:02d}".format(i))  # Dernier nombre, suivi d'un saut de ligne
