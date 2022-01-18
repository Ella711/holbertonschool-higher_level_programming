#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    if fct is not None:
        try:
            return fct(*args)
        except (TypeError, ValueError, IndexError, ZeroDivisionError) as err:
            print("Exception: {}\n".format(err), file=sys.stderr)
            return None
