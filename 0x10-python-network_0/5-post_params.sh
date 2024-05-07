#!/bin/bash

# Check if URL is provided
if [ "$#" -ne 1 ]; then
	    echo "Usage: $0 <url>"
	        exit 1
fi

# Send a POST request to the URL with the specified variables and display the body of the response
curl -s -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" $1
