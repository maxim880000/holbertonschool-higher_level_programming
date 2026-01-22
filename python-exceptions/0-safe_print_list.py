#!/usr/bin/python3
# fonction qui imprime au plus x éléments d'une liste
def safe_print_list(my_list=[], x=0):
    count = 0  # compteur pour le nombre d'éléments imprimés

    for i in range(x):  # on essaie d'imprimer x éléments
        try:
            print(my_list[i], end='')  # imprime l'éléments
            count += 1  # on incrémente le compteur
        except IndexError:  # si on dépasse la longueur de la liste
            break  # on arrête la boucle

    print()  # saut de ligne après tous les éléments imprimés
    return count  # retourne le nombre réel d'éléments imprimés
