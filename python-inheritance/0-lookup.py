#!/usr/bin/python3
"""
Defines a function that returns the list
of available attributes and methods of an object
"""

def lookup(obj):
    """return the list of available attributes and methods of an object
    thank to the fonction dir"""
    return (dir(obj))
