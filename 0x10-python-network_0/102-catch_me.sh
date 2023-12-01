#!/bin/bash

# Make a request to 0.0.0.0:5000/catch_me with curl
curl -sLX PUT --header "Origin: HolbertonSchool" -d "user_id=98" 0.0.0.0:5000/catch_me

