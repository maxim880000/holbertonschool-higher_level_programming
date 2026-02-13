#!/usr/bin/env python3
"""Module pour convertir un fichier CSV en JSON."""

# Import du module csv pour lire des fichiers CSV
# Import du module json pour sérialiser les données en JSON
import csv
import json


def convert_csv_to_json(csv_filename):
    """Convertit les données d'un fichier CSV en JSON et les écrit dans data.json.

    Args:
        csv_filename (str): Nom du fichier CSV à lire.

    Returns:
        bool: True si la conversion a réussi, False sinon.
    """
    try:
        # Liste qui va contenir chaque ligne du CSV sous forme de dictionnaire
        data_list = []

        # Ouverture du fichier CSV en lecture
        with open(csv_filename, newline='', encoding='utf-8') as csvfile:
            # DictReader convertit chaque ligne en dictionnaire {colonne: valeur}
            reader = csv.DictReader(csvfile)

            # On parcourt chaque ligne et on l'ajoute à la liste
            for row in reader:
                data_list.append(row)

        # Ouverture du fichier data.json en écriture pour sauvegarder le JSON
        with open('data.json', 'w', encoding='utf-8') as jsonfile:
            # On convertit la liste de dictionnaires en JSON et on écrit dans le fichier
            json.dump(data_list, jsonfile, indent=4)

        return True

    except FileNotFoundError:
        # Si le fichier CSV n'existe pas, on retourne False
        print(f"Erreur : le fichier {csv_filename} n'existe pas.")
        return False
