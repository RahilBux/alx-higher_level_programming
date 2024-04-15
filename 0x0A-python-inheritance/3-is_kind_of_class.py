#!/usr/bin/python3
"""Module for function is_kind_of_class"""


def is_kind_of_class(obj, a_class):
    """checks if obj is an instance of  a class or
    an instance of a class that inherited from specific class
    Args:
        obj: object to check
        a_class: class to compare
    Return:
        True or False
    """
    return isinstance(obj, a_class)
