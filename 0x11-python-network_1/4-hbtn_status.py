#!/usr/bin/python3
"""
Python script that fetches https://intranet.hbtn.io/status
    - You must use the package requests
    - You are not allowed to import packages other than requests
    - The body of the response must be displayed like the
    following example (tabulation before -)
"""
import requests


if __name__ == "__main__":

    body = requests.get("https://intranet.hbtn.io/status")
    print("Body response:")
    print("\t- type: {}".format(type(body.text)))
    print("\t- content: {}".format(body.text))
