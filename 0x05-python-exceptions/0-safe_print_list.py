#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    num1 = 0
    for i in my_list:
        if x > 0:
            try:
                print(i, end="")
                num1 += 1
                x -= 1
            except IndexError:
                break
    print("")
    return num1
