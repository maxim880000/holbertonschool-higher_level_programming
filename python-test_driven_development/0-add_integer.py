#!/usr/bin/python3
"""
This module provides a function to add two integers.

The function handles integers and floats, casting floats to integers
before performing the addition.
"""


def add_integer(a, b=98):
    """
    Add two integers or floats (casted to integers).

    Raises a TypeError if a or b is not an integer or a float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
