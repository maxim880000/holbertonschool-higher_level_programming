#!/usr/bin/python3
"""Module that reads a UTF-8 text file and prints it to stdout"""
# file: vraible qui represente le fichier ouvert


def read_file(filename=""):
    """reads a text file (UTF8) and prints it to stdout"""
    with open(filename, "r", encoding="utf-8") as file:
        print(file.read())
