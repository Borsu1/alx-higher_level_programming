#!/bin/bash

# Check if URL is provided
if [ "$#" -ne 1 ]; then
	    echo "Usage: $0 <url>"
	        exit 1
fi

# Send a GET request to the URL and display the body of the response if the status code is 200
response=$(curl -s -o /dev/null -w "%{http_code}" $1)
if [ "$response" -eq 200 ]; then
	    curl -s $1
    else
	        echo "The request did not return a 200 status code. It returned a status code of $response."
fi
