#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        if len(row) > 0:
            for i in range(len(row)):
                if i < len(low) - 1:
                    print("{:d}".format(row[i]), end=" ")
                else:
                    print("{:d}".format(row[i]), end="")
        print()
