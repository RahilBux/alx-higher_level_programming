#!/bin/bash
# Script that takes in a URL, sends a request and displays size of the body
curl -s "$1" | wc -c
