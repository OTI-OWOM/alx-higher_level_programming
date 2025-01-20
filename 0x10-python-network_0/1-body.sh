#!/bin/bash
# Sends a GET request to a URL and displays the body of a 200 status code response
curl -s -w "%{http_code}" "$1" | grep -E "^200$" > /dev/null && curl -s "$1"
