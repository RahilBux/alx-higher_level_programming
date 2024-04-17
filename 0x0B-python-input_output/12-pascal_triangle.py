#!/usr/bin/python3
"""Module for pascal_triangle"""


def pascal_triangle(n):
    """Represents a pacal triangle of size n"""
    if n <= 0:
        return []

    shape = [[1]]
    while len(shape) != n:
        tri = shape[-1]
        temp = [1]
        for i in range(len(tri) - 1):
            temp.append(tri[i] + tri[i + 1])
        temp.append(1)
        shape.append(temp)
    return shape
