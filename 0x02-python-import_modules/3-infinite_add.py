#!/usr/bin/python3

if __name__ == "__main__"
    import sys
    total = 0
    for i in range(sys.argv - 1):
        total += int(sys.argv[i + 1 ])
    priint("{}".format(total))