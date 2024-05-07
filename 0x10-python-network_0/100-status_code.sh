#!/bin/bash
#Bash script that sends a request to a URL passed as an argument, and displays only the status code of the response
# Check if URL is provided
if [ "$#" -ne 1 ]; then
	    echo "Usage: $0 <url>"
	        exit 1
fi

# Send a request to the URL and display only the status code of the response
curl -s -o /dev/null -w "%{http_code}" $1
