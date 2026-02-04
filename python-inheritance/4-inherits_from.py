#!/usr/bin/python3

def inherits_from(obj, a_class):
    """return True if the object is an instance
    of a class that inherited (directly or indirectly)
    from the specified class ; otherwise False"""
    # check que obj est une instance d’une sous-classe de a_class
    # mais pas une instance directe de a_class
    if isinstance(obj, a_class) and type(obj) is not a_class:
        return (True)
    else:
        return (False)
