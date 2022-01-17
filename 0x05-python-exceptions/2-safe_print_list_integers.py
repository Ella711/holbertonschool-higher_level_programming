#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    if my_list is not None:
        i = 0
        num_printed = 0
        while i < x:
            try:
                print("{:d}".format(my_list[i]), end="")
                i += 1
                num_printed += 1
            except (ValueError, TypeError):
                i += 1
            except IndexError:
                break
        print()
        return num_printed
    return None
