#!/bin/bash
# Script that takes a URL as an argument, sends a GET request, and displays body of response
curl -s "$1" -H "X-School-User-Id: 98"
