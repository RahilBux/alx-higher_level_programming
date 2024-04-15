#!/usr/bin/python3
"""Definition of function that checks if obj is instance of class"""


def is_same_class(obj, a_class):
    """checks if obj is an instance of class
    Args:
        obj: the object to check
        a_class: the class to match
    Returns:
        if obj is an instance True if not False
    """
    if type(obj) is a_class:
        return True
    return False
