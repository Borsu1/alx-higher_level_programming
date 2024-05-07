#!/bin/bash
#Bash script that sends a JSON POST request to a URL passed as the first argument, and displays the body of the response
# Check if both arguments are provided
if [ "$#" -ne 2 ]; then
	    echo "Usage: $0 <url> <filename>"
	        exit 1
fi

# Assign arguments to variables for better readability
url=$1
filename=$2

# Use curl to send a POST request
curl -s -X POST -H "Content-Type: application/json" -d @"$filename" "$url"
