#!/usr/bin/python3
def roman_to_int(roman_string: str):
    if roman_string is None or type(roman_string) is not str:
        return 0
    dictionary = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500,
                  'M': 1000}
    num = [dictionary[i] for i in roman_string] + [0]
    add = 0
    for i in range(len(num) - 1):
        if num[i] >= num[i + 1]:
            add += num[i]
        else:
            add -= num[i]
    return add
