#!/bin/bash

# Make a request to the URL and cause the server to respond with a message containing "You got me!"
curl -sLX PUT -d "user_id=98" -H "Origin: HolbertonSchool" 0.0.0.0:5000/catch_me
