#!/usr/bin/python3
"""Module for class MyInt"""


class MyInt(int):
    """MyInt reverses order of ints"""
    def __new__(cls, *args, **kwargs):
        """Creates instance of class"""
        return (super(MyInt, cls).__new__(cls, *args, **kwargs))

    def __eq__(self, other):
        """!= now =="""
        return (int(self) != other)

    def __ne__(self, other):
        """== now !="""
        return (int(self) == other)
