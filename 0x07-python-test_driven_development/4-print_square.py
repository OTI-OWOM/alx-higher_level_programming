#!/usr/bin/python3
""" This module contains a function that prints a square. """


def print_square(size):
    """prints a square with the character #

    Args:
        size (int): This size of the square.

    Raises:
        TypeError: If size is not an interger.
        ValueError: If size is  negative number.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        if isinstance(size, float):
            raise TypeError("size must be an integer")
        else:
            raise ValueError("size must be >= 0")
    for _ in range(int(size)):
        print("#" * size)
