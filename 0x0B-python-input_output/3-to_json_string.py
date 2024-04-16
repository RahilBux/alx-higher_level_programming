#!/usr/bin/python3
"""Module for to_json_string function"""
import json


def to_json_string(my_obj):
    """Function that returns the JSON rep of an obj
    Args:
        my_obj: Object to serialize
    """
    return json.dumps(my_obj)
