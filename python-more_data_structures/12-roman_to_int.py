#!/usr/bin/python3
# fonction qui convertit un chiffre romain en entier
def roman_to_int(roman_string):
    # vérifie que l'entrée est bien une chaîne
    if not isinstance(roman_string, str) or roman_string is None:
        return 0  # si ce n'est pas une chaîne, retourne 0

    # dictionnaire avec la valeur de chaque symbole romain
    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                  'C': 100, 'D': 500, 'M': 1000}

    total = 0  # variable pour stocker le résultat final
    prev_value = 0  # variable pour stocker la valeur précédente

    # on parcourt la chaîne de la fin vers le début
    # parcours inversé pour gérer la soustraction
    for char in reversed(roman_string):
        # récupère la valeur du symbole, 0 si symbole inconnu
        value = roman_dict.get(char, 0)
        if value < prev_value:  # si le symbole est avant un symbole plus grand
            total -= value  # on soustrait
        else:
            total += value  # sinon on additionne
        prev_value = value  # on met à jour la valeur précédente

    return total  # retourne le nombre final
