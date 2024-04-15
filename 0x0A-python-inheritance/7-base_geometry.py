#!/usr/bin/python3
""" Module for Class BaseGeometry"""


class BaseGeometry:
    """Initialize class BaseGeometry"""
    def area(self):
        """Returns area"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Method to validate value"""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
