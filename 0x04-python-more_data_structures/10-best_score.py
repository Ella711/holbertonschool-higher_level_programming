#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is not None:
        for key in a_dictionary:
            best = max(a_dictionary.items())
        return best[0]

# return(max(a_dictionary, key=a_dictionary.get))
