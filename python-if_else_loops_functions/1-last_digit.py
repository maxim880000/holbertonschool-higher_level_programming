#!/usr/bin/python3
# import random (generates nb)
import random
# .randint generate nb between a and b
number = random.randint(-10000, 10000)

# recup the last digit
# abs(number) recup the absolute value +
last_digit = abs(number) % 10

# if negatif add -
if number < 0:
    last_digit = -last_digit

# Affiche le nombre et son dernier chiffre
print(f"Last digit of {number} is {last_digit}", end=" ")

if last_digit > 5:
    print("and is greater than 5")

elif last_digit == 0:
    print("and is 0")

# le dernier chiffre est inférieur à 6
# et il n’est pas égal à 0
else:
    print("and is less than 6 and not 0")
