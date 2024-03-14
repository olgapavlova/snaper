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


window = Window(10)
window.start_driver()
window.open_page('https://www.producthunt.com')
img = window.screenshot_full_page()
print(type(img))