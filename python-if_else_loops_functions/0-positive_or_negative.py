#!/usr/bin/python3
import random
# import random (generates nb)
# .randint generate nb between a and b
number = random.randint(-10, 10)

if number > 0:
    print(number, "is positive")
elif number < 0:
    print(number, "is negative")
else:
    print(number, "is zero")
