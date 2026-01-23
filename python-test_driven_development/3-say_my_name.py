#!/usr/bin/python3
# This module provides a function that prints a formatted name.
# The function prints a sentence using a first name and a last name

def say_my_name(first_name, last_name=""):
# Print a sentence with the given first and last name.

    # Vérifie que le prénom est une chaîne de caractères
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    # Vérifie que le nom est une chaîne de caractères
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    # Affiche la phrase avec le prénom et le nom
    print("My name is {} {}".format(first_name, last_name))
