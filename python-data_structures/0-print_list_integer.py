#!/usr/bin/python3
# prints all integers of a list.
def print_list_integer(my_list=[]):
    # Boucle pour parcourir chaque élément de la liste
    for i in my_list:
        # Affiche l'entier avec le format {:d}
        print("{:d}".format(i))
