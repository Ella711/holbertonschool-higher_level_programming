#!/bin/bash
# Script that takes in a URL as an argument, sends a GET request to the URL, and displays the body of the response
# A variable email must be sent with the value test@gmail.com
# A variable subject must be sent with the value I will always be here for PLD
curl -X POST -F 'email=test@gmail.com' -F 'subject=I will always be here for PLD' "$1"
