#!/usr/bin/python3
import json
# returns the JSON representation of an object (string)


def to_json_string(my_obj):
    # Transforme l'objet Python en texte pour le partager/sauvegarder
    return json.dumps(my_obj)
