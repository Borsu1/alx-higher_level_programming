heck if URL and filename are provided
if [ "$#" -ne 2 ]; then
	    echo "Usage: $0 <url> <filename>"
	        exit 1
fi

# Send a JSON POST request to the URL with the contents of a file and display the body of the response
curl -s -X POST -H "Content-Type: application/json" -d @${2} $1
