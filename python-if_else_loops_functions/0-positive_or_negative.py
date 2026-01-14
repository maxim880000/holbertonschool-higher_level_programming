#!/usr/bin/python3
import random
# On importe le module random pour pouvoir générer des nombres aléatoires
number = random.randint(-10, 10)

if number > 0:
    print(number, "is positive")
elif number < 0:
    print(number, "is negative")
else:
    print(number, "is zero")
