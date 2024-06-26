#!/bin/bash
#Bash script that sends a DELETE request to the URL passed as the first argument and displays the body of the response
# Check if URL is provided
if [ "$#" -ne 1 ]; then
	    echo "Usage: $0 <url>"
	        exit 1
fi

# Send a DELETE request to the URL and display the body of the response
curl -s -X DELETE $1
