#!/usr/bin/python3
# Fonction qui trouve tous les multiples de 2 dans une liste
def divisible_by_2(my_list=[]):
    # Crée une nouvelle liste pour stocker les résultats
    result = []
    # Parcourt chaque nombre de la liste
    for num in my_list:
        # Vérifie si le nombre est divisible par 2 et ajoute True ou False
        result.append(num % 2 == 0)
    # Retourne la liste de résultats
    return result
