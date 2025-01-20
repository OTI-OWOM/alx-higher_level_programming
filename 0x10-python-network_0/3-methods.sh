#!/bin/bash
# Script to display HTTP methods supported by a server
curl -sI -X OPTIONS http://localhost:5000 | grep -i "allow:" | cut -d: -f2 | tr -d ' ' | tr ',' '\n'
