#!/bin/bash
# Displays the size of the body response from a given URL using curl
curl -s -o /dev/null -w "%{size_download}" "$1"
