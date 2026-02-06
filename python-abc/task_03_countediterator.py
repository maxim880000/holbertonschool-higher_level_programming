#!/usr/bin/env python3

class CountedIterator:
    """
    Iterator qui enveloppe un iterable et compte le nombre
    d'éléments réellement consommés via __next__.
    """

    def __init__(self, iterable):
        """
        Initialise l'iterator.

        :param iterable: n'importe quel objet
        itérable (liste, tuple, générateur, etc.)
        """
        # On transforme l'iterable en iterator une seule fois
        # (erreur classique : appeler iter() dans __next__)
        self._iterator = iter(iterable)

        # Compteur interne du nombre d'éléments retournés
        self._count = 0

    def __iter__(self):
        """
        Un iterator doit retourner lui-même dans __iter__.
        Cela permet l'utilisation dans une boucle for.
        """
        return self

    def __next__(self):
        """
        Retourne l'élément suivant et incrémente le compteur.

        L'appel à next(self._iterator) peut lever StopIteration.
        Si c'est le cas,le compteur ne doit PAS être incrémenté.
        """
        # On récupère l'élément suivant(StopIteration propagée automatiquement)
        item = next(self._iterator)

        # On incrémente le compteur uniquement si l'élément existe
        self._count += 1

        return item

    def get_count(self):
        """
        Retourne le nombre d'éléments déjà itérés.
        """
        return self._count
