#!/usr/bin/python3

class MyList(list):
    """class qui herite de list"""
    def print_sorted(self):
        """print la list & (trier dans l'odre croissant)"""
        print(sorted(self))
