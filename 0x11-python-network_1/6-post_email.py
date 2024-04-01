#!/usr/bin/python3
"""Sends a POST request to the passed URL with the email as a parameter"""

import urllib.parse
import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    DATA = urllib.parse.urlencode({"email": email}).encode()
    req = urllib.request.Request(url, data=DATA, method="POST")
    with urllib.request.urlopen(req) as response:
        print(response.read().decode("utf-8"))
