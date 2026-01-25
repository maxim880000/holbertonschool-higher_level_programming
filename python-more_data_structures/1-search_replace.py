#!/usr/bin/python3
# Fonction qui remplace toutes les occurrences d'un élément par un autre
def search_replace(my_list, search, replace):
    # crée et retourne une nouvelle liste où chaque élément égal à 
	# search est remplacé par replace, les autres restent identiques.
    return [replace if item == search else item for item in my_list]
