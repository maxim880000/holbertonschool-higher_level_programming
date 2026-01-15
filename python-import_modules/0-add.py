#!/usr/bin/python3

# Importe uniquement la fonction add depuis le fichier add_0
from add_0 import add

# Vérifie que le fichier est exécuté directement et non importé
if __name__ == "__main__":
    # Assigne la valeur 1 à la variable a
    a = 1
    # Assigne la valeur 2 à la variable b
    b = 2
    # Affiche le calcul et le résultat au format demandé
    print("{} + {} = {}".format(a, b, add(a, b)))
