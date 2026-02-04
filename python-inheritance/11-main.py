#!/usr/bin/python3
"""
Script de test pour la classe Square (11-square.py)
"""
Square = __import__('11-square').Square

if __name__ == "__main__":
    s = Square(13)
    print(s)
    print(s.area())
