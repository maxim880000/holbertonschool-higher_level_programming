#!/usr/bin/python3
# Importe la fonction add depuis le fichier add_0.py
from add_0 import add

# Vérifie que le fichier est exécuté directement
# et pas importé depuis un autre fichier
if __name__ == "__main__":
    # Déclaration de la première variable
    a = 1

    # Déclaration de la deuxième variable
    b = 2

    # Affiche le calcul et le résultat de l'addition
    print("{} + {} = {}".format(a, b, add(a, b)))
