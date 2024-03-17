#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new_list = my_list[:]
    len1 = len(my_list) - 1
    while len1 >= 0:
        if new_list[len1] % 2 == 0:
            new_list[len1] = True
        else:
            new_list[len1] = False
        len1 -= 1
    return new_list
