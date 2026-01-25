#!/usr/bin/python3
# Fonction qui additionne tous les entiers uniques d'une liste
def uniq_add(my_list=[]):
    # convert in set to delete (doublons)
    # Puis additionne tous les éléments uniques avec sum()
    return sum(set(my_list))
