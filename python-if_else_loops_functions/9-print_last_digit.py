#!/usr/bin/python3
# prints the last digit of a number.
def print_last_digit(number):

    # abs pour les nb negatifs
    last_digit = abs(number) % 10
    # afficher le dernier chiffre sans saut de ligne
    print("{}".format(last_digit), end="")

    return last_digit
