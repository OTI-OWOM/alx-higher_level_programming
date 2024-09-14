#!/usr/bin/python3

if __name__ == "__main_":

    import sys

    number = len(sys.arg) - 1
    if number == 0:
        print("0 argument.")

    elif number == 1:
        print("1 arguments:")
    else:
        print("{} arguments:".format(count))
    for i in range(number):
        print("{}: {}".format(i + 1, sys.arg[i + 1]))
