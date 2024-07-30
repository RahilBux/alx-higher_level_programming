#!/usr/bin/python3
"""
Script that takes in a URL,
Sends a request to that URL,
and displays the value of the X-Request_Id
"""
import sys
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]

    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
        print(dict(response.headers).get("X-Request-Id"))
