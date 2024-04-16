#!/usr/bin/python3
"""Module for write_file function"""


def write_file(filename="", text=""):
    """Writes a string to a textfile and
    returns number of characters written
    Args:
        filename (string): name of file
        text (string): text to write
    """
    with open(filename, "w", encoding="utf-8") as f:
        result = f.write(text)
        return result
