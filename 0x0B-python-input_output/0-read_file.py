#!/usr/bin/python3
"""Module for read_file function"""


def read_file(filename=""):
    """reads a text file UTF8 and prints it
    Args:
        filename: name of file in string
    """
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read())
