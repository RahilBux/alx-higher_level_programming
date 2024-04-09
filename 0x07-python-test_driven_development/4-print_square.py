#!/usr/bin/python3
"""Defines a square printing function"""


def print_square(size):
    """Print a square using character "#"

    Args:
        size (int): the size of the square
    Raises:
        TypeError: if size isn't an integer
        ValueError: if size < 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        [print("#", end="") for j in range(size)]
        print("")
