#!/usr/bin/python3

def print_alternating_alphabet():
    print(''.join(chr(122 - i) if i % 2 == 0 else chr(89 - i) for i in range(26)), end="")
