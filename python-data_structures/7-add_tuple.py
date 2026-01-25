#!/usr/bin/python3
# Fonction qui additionne 2 tuples
def add_tuple(tuple_a=(), tuple_b=()):
    # Récupère le premier élément de tuple_a, ou 0 si absent
    a1 = tuple_a[0] if len(tuple_a) >= 1 else 0
    # Récupère le deuxième élément
    a2 = tuple_a[1] if len(tuple_a) >= 2 else 0
    # Récupère le premier élément de tuple_b, ou 0 si absent
    b1 = tuple_b[0] if len(tuple_b) >= 1 else 0
    # Récupère le deuxième élément
    b2 = tuple_b[1] if len(tuple_b) >= 2 else 0
    # Retourne un nouveau tuple avec les sommes
    return (a1 + b1, a2 + b2)
