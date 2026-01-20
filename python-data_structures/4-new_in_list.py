#!/usr/bin/python3
# Fonction qui remplace un élément dans une copie de la liste
def new_in_list(my_list, idx, element):
    # Vérifie si l'index est négatif ou hors limites
    if idx < 0 or idx >= len(my_list):
        # Retourne une copie de la liste originale
        return my_list.copy()
    # Crée une copie de la liste originale
    new_list = my_list.copy()
    # Remplace l'élément à l'index spécifié dans la copie
    new_list[idx] = element
    # Retourne la nouvelle liste modifiée
    return new_list
