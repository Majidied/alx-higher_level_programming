#!/usr/bin/python3
"""Fetches the last 10 commits from a given repository"""
import sys
import requests

if __name__ == "__main__":
    url = "https://api.github.com/repos/{}/{}/commits".format(sys.argv[2],
                                                            sys.argv[1])
    r = requests.get(url)
    commits = r.json()
    for commit in commits[:10]:
        print(
            "{}: {}".format(
                commit.get("sha"), commit.get("commit").get("author").get("name")
            )
        )
