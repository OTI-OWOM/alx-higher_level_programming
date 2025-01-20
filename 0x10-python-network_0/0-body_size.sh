#!/bin/bash

# Check if URL is provided as an argument
if [ $# -eq 0 ]; then
   echo "Please provide a URL"
   exit 1
fi

# Use curl to send a request and retrieve the body size in bytes
curl -s -o /dev/null -w "%{size_download}" "$1"
