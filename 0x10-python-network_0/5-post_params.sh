#!/bin/bash
# Script to send a POST request with email and subject parameters to validate
curl -s -X POST -d "email=test@gmail.com" -d "subject=I will always be here for PLD" "$1"
