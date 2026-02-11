#!/usr/bin/python3
"""writes a string to a text file (UTF8) and return nb of char"""
# 'w' ecrire dans un fichier


def write_file(filename="", text=""):
    """writes a string to a text file (UTF8) and return nb of char"""
    with open(filename, 'w', encoding="utf-8") as file:
        return file.write(text)
