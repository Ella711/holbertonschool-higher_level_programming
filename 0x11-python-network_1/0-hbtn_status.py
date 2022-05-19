#!/usr/bin/python3
"""
Python script that fetches https://intranet.hbtn.io/status
    - You must use the package urllib
    - You are not allowed to import any packages other than urllib
    - The body of the response must be displayed like
    the following example (tabulation before -)
    - You must use a with statement
"""
import urllib.request

req = urllib.request.Request('https://intranet.hbtn.io/status')
with urllib.request.urlopen(req) as response:
    html = response.read()
    print("""Body response:
    - type: {}
    - content: {}
    - utf8 content: {}""".format(type(html), html, html.decode("utf-8")))
