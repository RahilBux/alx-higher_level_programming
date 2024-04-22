#!/usr/bin/python3
"""Module for Square Object"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Represents the Square class"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize the square"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """size getter"""
        return self.width

    @size.setter
    def size(self, value):
        """size setter"""
        self.width = value
        self.height = value

    def __str__(self):
        """Returns the str Rep for str() and print()"""
        return "[Square] ({}) {}/{} - {}".format(self.id,
                                                 self.x,
                                                 self.y,
                                                 self.height)

    def update(self, *args, **kwargs):
        """Updates the square values"""
        if args and len(args) != 0:
            for i, argument in enumerate(args):
                if i == 0:
                    self.id = argument
                elif i == 1:
                    self.size = argument
                elif i == 2:
                    self.x = argument
                elif i == 3:
                    self.y = argument
                else:
                    break
        elif len(kwargs) > 0:
            for key, value in kwargs.items():
                if key == "id":
                    self.id == value
                elif key == "size":
                    self.size = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """Returns the dictionary rep of square"""
        square_dict = {"id": self.id,
                       "size": self.height,
                       "x": self.x,
                       "y": self.y}
        return square_dict
