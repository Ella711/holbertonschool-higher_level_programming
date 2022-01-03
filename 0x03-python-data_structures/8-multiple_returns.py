#!/usr/bin/python3
def multiple_returns(sentence):
    if not sentence:
        new_tuple = (len(sentence), None)
    else:
        new_tuple = (len(sentence), sentence[0])
    return new_tuple
