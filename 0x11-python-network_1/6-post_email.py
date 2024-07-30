#!/usr/bin/python3
"""
Script that takes URL and posts Email
"""
import requests
from sys import argv


if __name__ == "__main__":
    read = {"email": argv[2]}
    r = requests.post(argv[1], data=read)
    print(r.text)
