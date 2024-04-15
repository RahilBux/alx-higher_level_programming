#!/usr/bin/python3
""" Module for Class BaseGeometry"""


class BaseGeometry:
    """Initialize class BaseGeometry"""
    def area(self):
        """Returns area"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Method to validate value
        Args:
            name (str): the name of parameter
            value (int): value to validate
        Raises:
            TypeError: if value in not an int
            ValueError: if value is <= 0
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
