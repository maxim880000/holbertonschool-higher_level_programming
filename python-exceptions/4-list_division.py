#!/usr/bin/python3
# function that divides element by element two lists

def list_division(my_list_1, my_list_2, list_length):
    """Divides element by element two lists and handles errors"""
    result = []  # liste pour stocker les résultats

    for i in range(list_length):  # on parcourt jusqu'à list_length
        try:
            # essaie de diviser les éléments
            division = my_list_1[i] / my_list_2[i]
        except IndexError:  # si l'un des indices n'existe pas
            print("out of range")
            division = 0
        except ZeroDivisionError:  # si division par zéro
            print("division by 0")
            division = 0
        except (TypeError, ValueError):  # si un élément n'est pas nombre
            print("wrong type")
            division = 0
        finally:
            result.append(division)  # ajoute toujours le résultat à la liste

    return result  # retourne la nouvelle liste
