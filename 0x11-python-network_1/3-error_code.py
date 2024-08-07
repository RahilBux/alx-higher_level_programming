#!/usr/bin/python3
"""
Script that takes in a URL, sends a request and display body
"""

import sys
from urllib import request, error

if __name__ == "__main__":
    try:
        with request.urlopen(sys.argv[1]) as response:
            print(response.read().decode("utf-8"))
    except error.HTTPError as error:
        print("Error code:", error.code)
