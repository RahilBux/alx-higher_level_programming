#!/usr/bin/python3
"""Fetches status"""
import requests


if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    read = requests.get(url)
    text = read.text
    print("Body response:")
    print("\t- type: {}".format(type(text)))
    print("\t- content: {}".format(text))
