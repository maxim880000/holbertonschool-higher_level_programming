#!/usr/bin/python3

# Fonction qui affiche les nombres de 1 à 100
def fizzbuzz():
    # Boucle sur les nombres de 1 à 100 inclus
    for i in range(1, 101):
        # Si le nombre est multiple de 3 et de 5, on affiche FizzBuzz
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz", end=" ")
        # Si le nombre est multiple de 3 seulement, on affiche Fizz
        elif i % 3 == 0:
            print("Fizz", end=" ")
        # Si le nombre est multiple de 5 seulement, on affiche Buzz
        elif i % 5 == 0:
            print("Buzz", end=" ")
        # Sinon, on affiche simplement le nombre
        else:
            print("{}".format(i), end=" ")
