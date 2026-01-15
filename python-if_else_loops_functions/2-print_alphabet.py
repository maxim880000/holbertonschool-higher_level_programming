#!/usr/bin/python3

# Boucle de i = 97 (a) à 122 (z)
for i in range(97, 123):
    # On ignore les lettres e (101) et q (113)
    if i != 101 and i != 113:
        # On affiche le caractère correspondant à i sans saut de ligne
        print("{}".format(chr(i)), end="")
