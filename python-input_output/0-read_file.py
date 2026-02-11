#!/usr/bin/python3
# file: vraible qui represente le fichier ouvert
# UTF-8 sert a transformer les lettres en 0 et 1
# reads a text file (UTF8) and prints it to stdout:


def read_file(filename=""):
    """reads a text file (UTF8) and prints it to stdout"""
    with open(filename, encoding="utf-8") as file:
        # file.read lire tout le fichier
        print(file.read())
