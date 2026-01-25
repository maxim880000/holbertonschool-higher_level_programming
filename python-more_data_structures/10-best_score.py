#!/usr/bin/python3
# Cette fonction retourne la clé (le nom)
# qui a la plus grande valeur (le score)

def best_score(a_dictionary):
    # Si le dictionnaire est vide ou None
    if not a_dictionary:
        return None

    # Variable pour garder la meilleure clé
    best_key = None

    # Variable pour garder la meilleure valeur
    best_value = None

    # On parcourt chaque élément du dictionnaire
    for key, value in a_dictionary.items():
        # Si c'est la première valeur
        # ou si la valeur est plus grande que la précédente
        if best_value is None or value > best_value:
            best_value = value  # On met à jour la meilleure valeur
            best_key = key      # On met à jour la clé associée

    return best_key
