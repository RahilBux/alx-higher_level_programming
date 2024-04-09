#!/usr/bin/python3
"""Defines an addition function"""

def add_integer(a, b=98):
    """Return a + b

    Floats are typecasted to ints before added
    
    Raises:
        TypeError: if a or b are not ints or floats
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
