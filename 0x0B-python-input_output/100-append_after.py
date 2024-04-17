#!/usr/bin/python3
"""Module for append_after function"""


def append_after(filename="", search_string="", new_string=""):
    """Function that inserts text after each line with new string
    Args:
        filename: The name of file
        search_string: the string to search for in file
        new_string: new string to insert
    """
    string = ""
    with open(filename) as f:
        for i in f:
            string += i
            if search_string in i:
                string += new_string
    with open(filename, "w") as w:
        w.write(string)
