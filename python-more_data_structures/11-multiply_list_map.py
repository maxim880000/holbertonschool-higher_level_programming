#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    return list(map(lambda x: x * number, my_list))
	# multiplie chaque valeur et crée une nouvelle liste
    # map() applique cette fonction à chaque élément de la liste.