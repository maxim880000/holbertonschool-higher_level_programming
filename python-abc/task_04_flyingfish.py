#!/usr/bin/env python3

class Fish:
    """
    Classe représentant un poisson.
    """

    def swim(self):
        """
        Action de nager.
        """
        print("The fish is swimming")

    def habitat(self):
        """
        Habitat du poisson.
        """
        print("The fish lives in water")


class Bird:
    """
    Classe représentant un oiseau.
    """

    def fly(self):
        """
        Action de voler.
        """
        print("The bird is flying")

    def habitat(self):
        """
        Habitat de l'oiseau.
        """
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """
    Classe FlyingFish héritant à la fois de Fish et Bird.
    Exemple de multiple inheritance.
    """

    def swim(self):
        """
        Redéfinition de la méthode swim de Fish.
        """
        print("The flying fish is swimming!")

    def fly(self):
        """
        Redéfinition de la méthode fly de Bird.
        """
        print("The flying fish is soaring!")

    def habitat(self):
        """
        Redéfinition de la méthode habitat présente
        dans Fish ET Bird.
        """
        print("The flying fish lives both in water and the sky!")
