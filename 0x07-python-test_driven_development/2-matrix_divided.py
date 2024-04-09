#!/usr/bin/python3
"""Defines a matrix div function"""


def matrix_divided(matrix, div):
    """Divides all elements of the matrix

    Args:
        matrix (list): A list of lists containing ints or floats
        div (int or float): the divider
    Raises:
        TypeError: If the matrix contains characters that aren't real numbers
        TypeError: If the matrix cotains rows of differents sizes
        TypeError: if div isn't an int or a float
        ZeroDivisionError: If div = 0
    Returns:
        A new matrix with the results
    """
    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(i, list) for i in matrix) or
            not all((isinstance(j, int) or isinstance(j, float))
                    for j in [num for i in matrix for num in i])):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")

    if not all(len(i) == len(matrix[0]) for i in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return ([list(map(lambda x: round(x / div, 2), i)) for i in matrix])
