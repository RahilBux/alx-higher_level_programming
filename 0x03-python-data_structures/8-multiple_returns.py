#!/usr/bin/python3
def multiple_returns(sentence):
    len1 = len(sentence)
    if sentence == "":
        first = None
    else:
        first = sentence[0]
    return (len1, first)
