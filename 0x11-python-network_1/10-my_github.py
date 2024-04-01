#!/usr/bin/python3
"""Fetches my Github id"""
import sys
import requests

if __name__ == "__main__":
    url = "https://api.github.com/user"
    r = requests.get(url, auth=(sys.argv[1], sys.argv[2]), timeout=5)
    try:
        profile_info = r.json()
        print(profile_info['id'])
    except Exception:
        print('None')