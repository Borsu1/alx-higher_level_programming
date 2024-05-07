#!/bin/bash
#Bash script that takes in a URL and displays all HTTP methods the server will accept.
# Check if URL is provided
if [ "$#" -ne 1 ]; then
	    echo "Usage: $0 <url>"
	        exit 1
fi

# Send a request to the URL and display all HTTP methods the server will accept
curl -sI -X OPTIONS $1 | grep Allow | cut -d' ' -f2-
