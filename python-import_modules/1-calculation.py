#!/usr/bin/python3
# Importe les fonctions nécessaires depuis le fichier calculator_1.py
from calculator_1 import add, sub, mul, div

# Vérifie que le fichier est exécuté directement
# et non importé dans un autre script
if __name__ == "__main__":
    # Déclaration de la première variable
    a = 10

    # Déclaration de la deuxième variable
    b = 5

    # Affiche le résultat de l'addition
    print("{} + {} = {}".format(a, b, add(a, b)))

    # Affiche le résultat de la soustraction
    print("{} - {} = {}".format(a, b, sub(a, b)))

    # Affiche le résultat de la multiplication
    print("{} * {} = {}".format(a, b, mul(a, b)))

    # Affiche le résultat de la division
    print("{} / {} = {}".format(a, b, div(a, b)))
