#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    try:
        num = 0
        for i in x:
            print(my_list[i], end='')
            num++
        return num
    except IndexError:
        raise