#!/usr/bin/python3
# Cette ligne indique que le fichier doit être exécuté avec python3

def update_dictionary(a_dictionary, key, value):
    # Cette fonction prend trois paramètres :
    # a_dictionary : le dictionnaire à modifier
    # key : la clé (toujours une chaîne de caractères)
    # value : la valeur à associer à la clé (n'importe quel type)

    a_dictionary[key] = value
    # Cette ligne fait tout le travail :
    # - Si la clé existe déjà dans le dictionnaire, sa valeur est remplacée
    # - Si la clé n'existe pas, elle est créée avec la valeur donnée

    return a_dictionary
    # Cette ligne retourne le dictionnaire modifié
