#!/usr/bin/python3
"""Module for function inherits_from"""


def inherits_from(obj, a_class):
    """ function to check if obj is a class that inherits from a_class
    indirectly or directly
    Args:
        obj: object to check
        a_class: class to compare
    Return: True or False
    """
    if issubclass(type(obj), a_class) and type(obj) is not a_class:
        return True
    return False
