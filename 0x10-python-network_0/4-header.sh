heck if URL is provided
if [ "$#" -ne 1 ]; then
	    echo "Usage: $0 <url>"
	        exit 1
fi

# Send a GET request to the URL with a custom header and display the body of the response
curl -s -H "X-School-User-Id: 98" $1
