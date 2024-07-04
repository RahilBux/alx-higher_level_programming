#!/usr/bin/bash
# Script that takes in a URL, sends a request and displays size of the body
curl -sI "$1" | grep -i Content-length | cut -d " " -f 2
