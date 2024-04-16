#!/usr/bin/python3
"""Module for function from_json_string"""
import json


def from_json_string(my_str):
    """Function that returns an object represented by JSON string
    args:
        my_str: object
    """
    return json.loads(my_str)
