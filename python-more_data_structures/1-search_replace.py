#!/usr/bin/python3
# Fonction qui remplace toutes les occurrences d'un élément par un autre
def search_replace(my_list, search, replace):
    # Crée une nouvelle liste en remplaçant les éléments recherchés
    # Utilise une list comprehension pour parcourir et remplacer
    return [replace if item == search else item for item in my_list]
