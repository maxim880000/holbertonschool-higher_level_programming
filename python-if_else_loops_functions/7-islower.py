#!/usr/bin/python3

# Fonction qui vérifie si un caractère est en minuscule
def islower(c):
    # ord(c) retourne le code ASCII du caractère c
    # Les lettres minuscules vont de 'a' (97) à 'z' (122)
    if ord(c) >= 97 and ord(c) <= 122:
        return True  # Retourne True si c est compris entre 'a' et 'z'
    else:
        return False  # Retourne False sinon
