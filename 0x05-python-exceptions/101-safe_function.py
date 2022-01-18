#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    try:
        return fct(*args)
    except (TypeError, ValueError, IndexError, ZeroDivisionError) as err:
        print("Exception: {}".format(err), file=sys.stderr)
        return None
