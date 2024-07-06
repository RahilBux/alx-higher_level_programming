#!/usr/bin/python3
"""
Python script that takes URL
"""
import requests
from sys import argv

if __name__ == "__main__":
    read = requests.get(argv[1])
    print(read.headers.get("X-Request-Id"))
