#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    len1 = len(matrix)
    for i in range(len1):
        len2 = len(matrix[i])
        for j in range(len2):
            print('{}'.format(matrix[i][j]), end=" " if j != len2 - 1 else "")
        print("")
