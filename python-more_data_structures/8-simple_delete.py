#!/usr/bin/python3
# Cette ligne indique que le script doit être exécuté avec python3

def simple_delete(a_dictionary, key=""):
    # Cette fonction prend deux paramètres :
    # a_dictionary : le dictionnaire à modifier
    # key : la clé à supprimer (chaîne de caractères), vide par défaut

    if key in a_dictionary:
        # Cette condition vérifie si la clé existe dans le dictionnaire

        del a_dictionary[key]
        # Cette ligne supprime la clé et sa valeur du dictionnaire

    return a_dictionary
    # Cette ligne retourne le dictionnaire (modifié ou non)
