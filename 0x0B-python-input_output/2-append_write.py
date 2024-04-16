#!/usr/bin/python3
"""Module for append_write function"""


def append_write(filename="", text=""):
    """Appends text to a file
    Args:
        filename (str): name of file
        text (str): text to append
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
