#!/usr/bin/python3
# Fonction qui supprime un élément à une position spécifique
def delete_at(my_list=[], idx=0):
    # Vérifie si l'index est valide (positif et dans les limites)
    if idx >= 0 and idx < len(my_list):
        # Supprime l'élément en utilisant del
        del my_list[idx]
    # Retourne la liste modifiée
    return my_list
