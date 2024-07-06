#!/usr/bin/python3
"""
Python Script that takes in a URL,
sends a request and display body
"""
import requests
from sys import argv


if __name__ == "__main__":
    read = requests.get(argv[1])
    status = read.status_code
    if status < 400:
        print(read.text)
    else:
        print("Error code: {}".format(read.status_code)
