#!/usr/bin/python3
def upper(i):
    if ord(i) >= 97 and ord(i) <= 122:
        return (ord(i) - 32)
    else:
        return ord(i)


def uppercase(c):
    empty_string = ""
    for i in c:
        empty_string += "%c" % upper(i)
    print("{:s}".format(empty_string))
