#!/usr/bin/python3
# ecrit un string dans un fichier txt (return nb char)
# UTF-8 sert a transformer les lettres en 0 et 1
# 'w' ecrire dans un fichier


def write_file(filename="", text=""):
    with open(filename, 'w', encoding="utf-8") as file:
        file.write(text)
    return len(text)
