#!/usr/bin/python3
from sys import argv  # Pour récupérer les arguments passés au script

if __name__ == "__main__":
    total = 0  # On initialise le total à zéro

    # On parcourt tous les arguments sauf le nom du fichier
    for arg in argv[1:]:
        total += int(arg)
        # On convertit chaque argument en entier et on l'ajoute au total

    print(total)  # affiche le total
