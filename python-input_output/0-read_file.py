#!/usr/bin/python3
"""Module qui définit une fonction pour lire un fichier texte
et afficher son contenu sur la sortie standard.
"""


def read_file(filename=""):
    """Lit un fichier UTF-8 et affiche son contenu.

    Utilise l'instruction 'with' pour s'assurer que le fichier
    est fermé correctement après la lecture.
        filename (str): chemin du fichier à lire. Par défaut, vide.
    """
    # Ouverture du fichier en mode lecture ('r') avec encodage UTF-8
    with open(filename, 'r', encoding='utf-8') as f:
        # Lire tout le contenu du fichier et l'afficher
        print(f.read(), end="")  # end="" pour ne pas ajouter de nouvelle ligne supplémentaire
