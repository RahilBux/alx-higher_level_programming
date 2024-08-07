#!/usr/bin/python3
"""
Python script that takes in 2 args in order to solve challenge
"""
import requests
from sys import argv


if __name__ == "__main__":
    url = "https://api.github.com/repos/{}/{}/commits".format(argv[2], argv[1])
    re = requests.get(url)
    commits = re.json()
    for commit in commits[:10]:
        print(commit.get('sha'), end=': ')
        print(commit.get('commit').get('author').get('name'))
