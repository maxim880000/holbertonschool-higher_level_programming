#!/usr/bin/python3

def safe_print_integer(value):  # fonction qui essaie d'imprimer un entier
    try:
        print("{:d}".format(value))  # essaie d'imprimer la valeur comme entier
        return True  # si ça marche, retourne True
    # si ce n'est pas un entier, on attrape l'erreur
    except (ValueError, TypeError):
        return False  # retourne False si impression impossible
