#!/usr/bin/python3
def no_c(my_string):
    my_string_no_c_C = [i for i in my_string if i != 'c' or i != 'C']
    return ("".join(my_string_no_c_C))
