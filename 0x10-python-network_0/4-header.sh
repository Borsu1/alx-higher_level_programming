#!/bin/bash
#Write a Bash script that takes in a URL as an argument, sends a GET request to the URL, and displays the body of the response
# Check if URL was provided
if [ "$#" -ne 1 ]; then
	    echo "Usage: $0 <URL>"
	        exit 1
fi

URL=$1

# Send GET request with custom header
curl -s -H "X-School-User-Id: 98" "$URL"
