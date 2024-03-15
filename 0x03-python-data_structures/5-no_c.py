#!/usr/bin/python3
def no_c(my_string):
    new = ""
    for i in my_string:
        if ord(i) == ord('c') or ord(i) == ord('C'):
            continue
        new = new + i
    return new
