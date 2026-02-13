#!/usr/bin/env python3
"""Module pour sérialiser et désérialiser un dictionnaire en XML."""

# On importe ElementTree pour créer, écrire et lire du XML
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """Sérialise un dictionnaire Python en fichier XML.

    Args:
        dictionary (dict): Dictionnaire à convertir.
        filename (str): Nom du fichier XML de sortie.
    """
    # Création de l'élément racine <data>
    root = ET.Element("data")

    # On ajoute chaque paire clé/valeur comme sous-élément
    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)  # XML stocke du texte uniquement

    # Création de l'arbre XML
    tree = ET.ElementTree(root)

    # Écriture dans le fichier
    tree.write(filename, encoding="utf-8", xml_declaration=True)


def deserialize_from_xml(filename):
    """Désérialise un fichier XML en dictionnaire Python.

    Args:
        filename (str): Nom du fichier XML à lire.

    Returns:
        dict: Dictionnaire reconstruit depuis le XML.
    """
    try:
        # Lecture et parsing du fichier XML
        tree = ET.parse(filename)
        root = tree.getroot()

        # Reconstruction du dictionnaire
        result = {}

        for child in root:
            result[child.tag] = child.text

        return result

    except (ET.ParseError, FileNotFoundError):
        return None
