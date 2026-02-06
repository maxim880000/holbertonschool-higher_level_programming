#!/usr/bin/env python3

class SwimMixin:
    """
    Mixin apportant la capacité de nager.
    Un mixin n'est PAS censé être utilisé seul.
    """

    def swim(self):
        """
        Méthode ajoutant le comportement 'nager'.
        """
        print("The creature swims!")


class FlyMixin:
    """
    Mixin apportant la capacité de voler.
    """

    def fly(self):
        """
        Méthode ajoutant le comportement 'voler'.
        """
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """
    Classe Dragon qui combine plusieurs comportements
    via des mixins.
    """

    def roar(self):
        """
        Comportement spécifique au dragon.
        """
        print("The dragon roars!")
