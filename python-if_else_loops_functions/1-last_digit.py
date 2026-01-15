#!/usr/bin/python3
# Import random générer des nombres aléatoires
import random

# Génère un nombre aléatoire compris entre -10000 et 10000
number = random.randint(-10000, 10000)

# On récupère le dernier chiffre du nombre
# abs(number) permet d'éviter les problèmes avec les nombres négatifs
last_digit = abs(number) % 10

# Si le nombre est négatif,dernier chiffre doit aussi être négatif
# ex-123 -> = -3
if number < 0:
    last_digit = -last_digit

# Affiche le nombre et son dernier chiffre
# end=" " permet de continuer l'affichage sur la même ligne
print(f"Last digit of {number} is {last_digit}", end=" ")

if last_digit > 5:
    print("and is greater than 5")

elif last_digit == 0:
    print("and is 0")

# - le dernier chiffre est inférieur à 6
# - et il n’est pas égal à 0
else:
    print("and is less than 6 and not 0")
