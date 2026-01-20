#!/usr/bin/python3
# replaces an element at a specific position
def replace_in_list(my_list, idx, element):
    # Si l'index est négatif
    if idx < 0:
        return my_list

    # Si l'index est supérieur ou égal à la taille de la liste
    if idx >= len(my_list):
        return my_list

    # On remplace l'élément à la position idx
    my_list[idx] = element

    # On retourne la liste modifiée
    return my_list
