#!/usr/bin/python3
import json
# return un objet représenté par une chaîne JSON


def from_json_string(my_str):
    # JSON (texte) → Python
    return json.loads(my_str)
