#!/usr/bin/python3
"""Module for find_peak function"""


def find_peak(list_of_integers):
    """
    Function that finds a Peak in a list_of_integers

    Args:
        list_of_integers (list): A list of integers

    Returns:
        int: Peak in the list
    """
    copy = list_of_integers
    if copy == []:
        return None
    length = len(copy)

    begin, end = 0, length - 1
    while begin < end:
        mid = begin + (end - begin) // 2
        if copy[mid] > copy[mid - 1] and copy[mid] > copy[mid + 1]:
            return copy[mid]
        if copy[mid - 1] > copy[mid + 1]:
            end = mid
        else:
            begin = mid + 1
    return copy[begin]
