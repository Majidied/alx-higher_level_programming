#!/usr/bin/python3
"""Fetches https://intranet.hbtn.io/status"""
import urllib.request
import sys

if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as response:
        print(response.headers.get("X-Request-Id"))
