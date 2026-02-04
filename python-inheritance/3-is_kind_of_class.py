#!/usr/bin/python3
"""
Defines a function that checks if an object
is an instance of, or inherits from, a given class
"""


def is_kind_of_class(obj, a_class):
    """returns True if the object is an instance of, or if the object
    is an instance of a class that inherited from,
    the specified class ; otherwise False"""

    # check si obj est une instance de a_class
    if isinstance(obj, a_class):
        return (True)
    else:
        return (False)
