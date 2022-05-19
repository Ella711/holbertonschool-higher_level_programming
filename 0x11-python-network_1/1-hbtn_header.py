#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request to the URL and displays
the value of the X-Request-Id variable found in the header of the response.
    - You must use the packages urllib and sys
    - You are not allowed to import packages other than urllib and sys
    - The value of this variable is different for each request
    - You don’t need to check arguments passed to the script (number or type)
    - You must use a with statement
"""
from sys import argv
from urllib.request import Request, urlopen


if __name__ == "__main__":
    req = Request(argv[1])
    with urlopen(req) as response:
        print(response.getheader("X-Request-Id"))
