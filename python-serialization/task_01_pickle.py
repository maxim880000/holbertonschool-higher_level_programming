#!/usr/bin/env python3
"""Module pour sérialiser et désérialiser un objet Python personnalisé
en utilisant le module pickle.
"""

# On importe le module pickle pour transformer des objets Python
# en fichiers binaires et les reconstruire ensuite.
import pickle


class CustomObject:
    """Classe représentant un objet personnalisé avec un nom, un âge
    et un indicateur si c'est un étudiant.
    """


    def __init__(self, name, age, is_student):
        """Initialise une instance de CustomObject.

        Args:
            name (str): Nom de l'objet/personne.
            age (int): Âge de l'objet/personne.
            is_student (bool): Indique si l'objet est étudiant.
        """
        self.name = name
        self.age = age
        self.is_student = is_student


    def display(self):
        """Affiche les attributs de l'objet au format lisible."""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")


    def serialize(self, filename):
        """Sérialise l'objet et l'enregistre dans un fichier.

        Args:
            filename (str): Nom du fichier dans lequel sauvegarder l'objet.
        """
        try:
            with open(filename, 'wb') as file:
                # Ouverture du fichier en binaire pour écriture
                pickle.dump(self, file)  # Sauvegarde l'objet dans le fichier
        except (OSError, pickle.PicklingError) as e:
            print(f"Erreur lors de la sérialisation: {e}")

    @classmethod
    def deserialize(cls, filename):
        """Charge un objet sérialisé depuis un fichier et le retourne.

        Args:
            filename (str): Nom du fichier à lire.

        Returns:
            CustomObject: Une instance de l'objet chargée depuis le fichier,
            ou None si une erreur se produit.
        """
        try:
            with open(filename, 'rb') as file:
                # Ouverture du fichier en binaire pour lecture
                return pickle.load(file)  # Charge l'objet depuis le fichier
        except (OSError, pickle.UnpicklingError) as e:
            print(f"Erreur lors de la désérialisation: {e}")
            return None
