#!/usr/bin/python3
def remove_char_at(str, n):
    empty_string = ''
    index = 0
    for i in str:
        if index != n:
            empty_string += i
        index += 1
    return empty_string
