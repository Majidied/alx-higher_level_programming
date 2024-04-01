#!/usr/bin/python3
"""
Module  sends a POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter.
"""
from sys import argv
import requests


def main():
    """
    Script that takes in a letter and sends a POST request to
    http://0.0.0.0:5000/search_user with the letter as a parameter.
    """
    if len(argv) < 2:
        q = ""
    else:
        q = argv[1]
    payload = {"q": q}
    url = "http://0.0.0.0:5000/search_user"
    r = requests.post(url, data=payload, timeout=5)
    try:
        result = r.json()
        if not result:
            print("No result")
        else:
            print(f"[{result['id']}] {result['name']}")
    except ValueError:
        print("Not a valid JSON")


if __name__ == "__main__":
    main()
