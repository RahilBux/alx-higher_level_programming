#!/usr/bin/python3
"""Module for a rectangle class"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A subclass that represents a Rectangle"""
    def __init__(self, width, height):
        """Create the rectangle"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Returns the area"""
        return self.__width * self.__height

    def __str__(self):
        """str method to print"""
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))
