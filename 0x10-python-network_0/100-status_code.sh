#!/bin/bash
# Script that sends a request to a URL and displays only the status code of the response
curl -s -L -X HEAD -w "%{http_code}" "$1"
