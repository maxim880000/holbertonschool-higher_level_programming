#!/usr/bin/python3
# Fonction qui trouve le plus grand entier d'une liste
def max_integer(my_list=[]):
    # Retourne None si la liste est vide
    if len(my_list) == 0:
        return None
    # Initialise le maximum avec le premier élément
    max_value = my_list[0]
    # Parcourt chaque élément de la liste
    for num in my_list:
        # Compare et met à jour le maximum si nécessaire
        if num > max_value:
            max_value = num
    # Retourne la valeur maximale trouvée
    return max_value
