#!/usr/bin/python3
# fonction qui imprime les x premiers entiers d'une liste
def safe_print_list_integers(my_list=[], x=0):
    count = 0  # compteur pour le nombre d'entiers imprimés

    for i in range(x):  # essaie d'accéder aux x premiers éléments
        try:
            # imprime si c'est un entier
            print("{:d}".format(my_list[i]), end="")
            count += 1  # augmente le compteur si impression réussie
        except (ValueError, TypeError):  # si ce n'est pas un entier on ignore
            continue  # passe au suivant sans rien faire
        except IndexError:  # si on dépasse la longueur de la liste
            break  # on arrête la boucle

    print()  # saut de ligne après l'impression
    return count  # retourne le nombre réel d'entiers imprimés
