#!/usr/bin/python3
import json
# writes an Object to a text file, using a JSON representation
# Le but = sauvegarder dans un fichier


def save_to_json_file(my_obj, filename):
    with open(filename, 'w', encoding = "utf-8") as file:
        # json.dump(quoi, où)
        # transforme objpy en json et ecrit dans un fichier
        json.dump(my_obj, file)
