#!/usr/bin/python3
from sys import stderr


def safe_function(fct, *args):
    try:
        return fct(*args)
    except Exception as num:
        stderr.write("Exception: {}\n".format(num))
        return None
