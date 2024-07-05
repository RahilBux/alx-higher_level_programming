#!/usr/bin/python3
"""Script that takes in a URL and email,
sends a POST request and displays body of response
"""
import sys
import urllib.parse
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]
    val = {"email": sys.argv[2]}
    data = urllib.parse.urlencode(val).encode("ascii")

    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(request) as response:
        print(response.read().decode("utf-8"))
