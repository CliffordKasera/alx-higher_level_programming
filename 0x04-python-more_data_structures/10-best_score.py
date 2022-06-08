#!/usr/bin/python3

def best_score(a_dictionary):
    """Returns a key with the biggest integer value."""
    if not isinstance(a_dictionary, dict) or len(a_dictionary) == 0:
        return None

    biggest_key = list(a_dictionary.keys())[0]
    biggest_value = a_dictionary[biggest_key]
    for i, x in a_dictionary.items():
        if x > biggest_value:
            biggest_value = x
            biggest_key = i
    return (biggest_key)
