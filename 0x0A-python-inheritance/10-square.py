#!/usr/bin/python3
"""Module for a Square class"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """A Square Object"""
    def __init__(self, size):
        """Creates a Square Object"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Returns the Area"""
        return self.__size * self.__size
