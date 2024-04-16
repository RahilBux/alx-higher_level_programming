#!/usr/bin/python3
"""Module for function load_from_json_file"""
import json


def load_from_json_file(filename):
    """Creates a python object from a json file
    Args:
        filename: name of file    
    """
    with open(filename) as f:
        return json.load(f)
