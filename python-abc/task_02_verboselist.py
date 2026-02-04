#!/usr/bin/env python3
"""
Module définissant la classe VerboseList qui notifie lors des modifications.
"""

# Définition de la classe VerboseList qui hérite de list

class VerboseList(list):
    """
    Liste qui affiche un message à chaque modification (ajout, suppression).
    """
    def append(self, item):
        # Ajoute un élément à la liste et affiche un message
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, iterable):
        # Ajoute plusieurs éléments à la liste et affiche un message
        count = len(iterable)
        super().extend(iterable)
        print(f"Extended the list with [{count}] items.")

    def remove(self, item):
        # Affiche un message avant de retirer l'élément
        print(f"Removed [{item}] from the list.")
        super().remove(item)

    def pop(self, index=-1):
        # Affiche un message avant de retirer l'élément à l'index donné (ou le dernier)
        item = self[index]
        print(f"Popped [{item}] from the list.")
        return super().pop(index)
