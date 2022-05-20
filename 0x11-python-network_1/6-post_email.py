#!/usr/bin/python3
"""
Python script that takes in a URL and an email, sends a POST request
to the passed URL with the email as a parameter, and displays
the body of the response
    - The email must be sent in the email variable
    - You must use the packages requests and sys
    - You are not allowed to import packages other than requests and sys
    - You don’t need to check arguments passed to the script (number or type)
"""
import requests
from sys import argv


if __name__ == "__main__":
    values = {"email": argv[2]}

    body = requests.post(argv[1], values)
    print(body.text)
