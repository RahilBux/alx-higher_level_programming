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

    def to_json(self):
        return self.__dict__
