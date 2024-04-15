#!/usr/bin/python3
"""Definition of function add_attribute"""


def add_attribute(obj, attr, value):
    """Adds a new attribute to an object
    Args:
        obj: the object to add attr
        attr: attribute to add
        value: the value of attr
    Raises:
        TypeError: if attr can't be added
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, attr, value)
