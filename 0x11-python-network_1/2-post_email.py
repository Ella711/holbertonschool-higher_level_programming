#!/usr/bin/python3
"""
Python script that takes in a URL and an email, sends a POST request
to the passed URL with the email as a parameter, and displays
the body of the response (decoded in utf-8)
    - The email must be sent in the email variable
    - You must use the packages urllib and sys
    - You are not allowed to import packages other than urllib and sys
    - You don’t need to check arguments passed to the script (number or type)
    - You must use the with statement
"""
from sys import argv
from urllib.parse import urlencode
from urllib.request import Request, urlopen


if __name__ == "__main__":
    values = {"email": argv[2]}
    url_values_encoded = urlencode(values)
    post_values = url_values_encoded.encode("utf-8")

    req = Request(argv[1], post_values)
    with urlopen(req) as response:
        body = response.read()
        print(body.decode("utf-8"))
