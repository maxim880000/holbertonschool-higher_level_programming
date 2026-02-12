#!/usr/bin/python3
"""Script qui ajoute tous les arguments passés en ligne de commande
à une liste Python, puis sauvegarde cette liste dans un fichier JSON.
"""

import sys

# Import dynamique des fonctions demandées
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


filename = "add_item.json"

try:
    # On tente de charger la liste existante
    my_list = load_from_json_file(filename)
except FileNotFoundError:
    # Si le fichier n'existe pas, on initialise une liste vide
    my_list = []

# On ajoute tous les arguments passés en ligne de commande
# sys.argv[0] est le nom du script, donc on l'ignore
my_list.extend(sys.argv[1:])

# On sauvegarde la nouvelle liste dans le fichier JSON
save_to_json_file(my_list, filename)
