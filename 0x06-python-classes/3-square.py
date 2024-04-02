#!/usr/bin/python3
"""Class Square"""


class Square:
    """Square Rep"""

    def __init__(s, size=0):
        """New square
        Args:
            size (int): The size of side
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        s.__size = size
