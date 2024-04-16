#!/usr/bin/python3
"""Module for function save_to_json_file"""
import json


def save_to_json_file(my_obj, filename):
    """Function that writes an object to a text file using JSON
    Args:
        my_obj: object to write
        filename: file to write to
    """
    with open(filename, "w") as f:
        json.dump(my_obj, f)
