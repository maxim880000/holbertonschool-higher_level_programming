#!/usr/bin/python3

def simple_delete(a_dictionary, key=""):
# key : la clé à supprimer (chaîne de caractères)

    if key in a_dictionary:
        # Cette condition vérifie si la clé existe dans le dictionnaire

        del a_dictionary[key]
        # Cette ligne supprime la clé et sa valeur du dictionnaire

    return a_dictionary
    # Cette ligne retourne le dictionnaire (modifié ou non)
