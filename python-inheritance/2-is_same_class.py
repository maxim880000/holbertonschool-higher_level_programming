#!/usr/bin/python3

def is_same_class(obj, a_class):
    """True if the object is exactly an instance
    of the specified class ; otherwise False"""

    # define the type of obj and compare to class
    if type(obj) == a_class:
        return (True)
    else:
        return (False)
