#!/usr/bin/python3
"""
Script de test pour la classe Rectangle (9-rectangle.py)
"""
Rectangle = __import__('9-rectangle').Rectangle

if __name__ == "__main__":
    r = Rectangle(3, 5)
    print(r)
    print(r.area())
