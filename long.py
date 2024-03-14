import logging
from snaper.window import Window

# INIT section
logging.basicConfig(level=logging.INFO)


# FUNCTIONS

def L(function):
    '''Decorator to log some functions'''
    def wrapped(*args):
        logging.info(f"{function.__name__} starts --")
        result = function(*args)
        logging.info(f" -- stops")
        return result

    return wrapped
