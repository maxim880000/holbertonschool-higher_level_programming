#!/usr/bin/python3
from sys import argv
# On importe argv pour récupérer les arguments de la ligne de commande

if __name__ == "__main__":
    argc = len(argv) - 1
    # On calcule le nombre d’arguments (sans le nom du script)

    # Affichage de la première ligne selon le nombre d’arguments
    if argc == 0:
        print("0 arguments.")
    elif argc == 1:
        print("1 argument:")
    else:
        print(f"{argc} arguments:")

    # Boucle pour afficher chaque argument avec son numéro
    for i in range(1, len(argv)):  # On commence à 1 pass le nom du script
        print(f"{i}: {argv[i]}")  # Affiche le numéro et l’argument
