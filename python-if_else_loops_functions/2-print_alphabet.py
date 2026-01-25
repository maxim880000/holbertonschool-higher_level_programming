#!/usr/bin/python3
# Boucle sur les codes ASCII de 97 à 122 (a,z)
for i in range(97, 123):
    # chr(i) convertit le code ASCII en caractère
    print("{}".format(chr(i)), end="")
