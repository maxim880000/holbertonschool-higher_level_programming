#!/usr/bin/python3

def safe_print_division(a, b):  # fonction qui divise a par b
    result = None  # on initialise le résultat à None

    try:
        result = a / b  # essaie de diviser a par b
    except ZeroDivisionError:  # si b est zéro
        result = None  # impossible de diviser
    finally:
        # affiche le résultat dans finally
        print("Inside result: {}".format(result))

    return result  # retourne le résultat ou None si division impossible
