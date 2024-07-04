#!/bin/bash
# Script that takes in a URL, Sends POST request to the URL and displays the body of response
curl -s "$1" -X POST -d "email=test@gmail.com&subject=I will always be here for PLD"
