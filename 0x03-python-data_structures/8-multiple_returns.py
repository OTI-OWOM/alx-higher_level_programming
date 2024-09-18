#!/usr/bin/python3

def multiple_returns(sentence):
    for char in sentence:
        if len(char) == 0:
            return None
        else:
            return char
