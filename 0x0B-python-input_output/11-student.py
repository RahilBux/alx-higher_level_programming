#!/usr/bin/python3
"""Definition of Student class"""


class Student:
    """Student class object"""
    def __init__(self, first_name, last_name, age):
        """Initialize class
        Args:
            first_name: first name of student
            last_name: last name of student
            age: age of student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Gets the dictionary rep of the Student instance
        Args:
            attrs: the attributes
        """
        if (type(attrs) is list and all(type(i) is str for i in attrs)):
            return {j: getattr(self, j) for j in attrs if hasattr(self, j)}
        return self.__dict__

    def reload_from_json(self, json):
        """Replace all attributes
        Args:
            json: The key value pairs to replace
        """
        for i, j in json.items():
            setattr(self, i, j)
