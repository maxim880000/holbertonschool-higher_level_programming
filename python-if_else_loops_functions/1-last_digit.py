#!/usr/bin/python3
import random
# random number display his last digit
# Génère un nombre aléatoire
number = random.randint(-10000, 10000)

# % 10 donne le dernier chiffre
last_digit = number % 10

# On corrige pour avoir le vrai dernier chiffre avec le signe
if number < 0:
    last_digit = -last_digit   # -626 → on veut -6 et pas 4

# Affichage de la phrase de base
print(f"Last digit of {number} is {last_digit}", end=" ")

# différentes conditions demandées
if last_digit > 5:
    print("and is greater than 5")

elif last_digit == 0:
    print("and is 0")

else:
    # Ici on a soit :
    #    1,2,3,4,5 ou -1,-2,-3,-4,-5
    print("and is less than 6 and not 0")
