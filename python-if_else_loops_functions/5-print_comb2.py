#!/usr/bin/python3

for i in range(100): # Boucle de 0 à 99
    if i != 99:
        # {:02d} 2 chiffres avec un zéro devant
        print("{:02d}, ".format(i), end="")
    else:
        # Dernier nombre, suivi d'un saut de ligne
        print("{:02d}".format(i))
