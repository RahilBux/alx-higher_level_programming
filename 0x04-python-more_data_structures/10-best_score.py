#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary == None:
        return None
    result = 0
    name = ""
    for key, value in a_dictionary.items():
        if result < value:
            result = value
            name = key
    return name
