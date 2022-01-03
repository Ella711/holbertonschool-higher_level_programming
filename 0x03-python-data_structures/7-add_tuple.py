#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_b) == 1:
        tuple_b_list = list(tuple_b)
        tuple_b_list.append(0)
        tuple_b = tuple(tuple_b_list)
        return tuple(map(lambda x, y: x + y, tuple_a, tuple_b))
    elif len(tuple_b) == 0:
        tuple_b_list = list(tuple_b)
        tuple_b_list = [0, 0]
        tuple_b = tuple(tuple_b_list)
        return tuple(map(lambda x, y: x + y, tuple_a, tuple_b))
    else:
        return tuple(map(lambda x, y: x + y, tuple_a, tuple_b))
