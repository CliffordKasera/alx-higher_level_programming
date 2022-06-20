#!/usr/bin/python3

def raise_exception():
    try:
        num = "Test error"
        num[3] = "ok"
    except TypeError:
        print("Exception raised")
        raise
