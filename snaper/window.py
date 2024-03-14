from selenium import webdriver

class Window:
    '''Browser window, its config and operations'''
    def __init__(self, wait_in_seconds) -> None:
        self.wait_in_seconds = wait_in_seconds

    def start_driver(self):
        self.driver = webdriver.Chrome()

    def set_window_size(self, width, height):
        self.driver.set_window_size(width=width, height=height)

    def set_window_width_but_keep_height(self, width):
        height = self.driver.get_window_size()['height']
        self.set_window_size(width, height)


if __name__ == "__main__":

    window = Window(10)
    assert window.wait_in_seconds == 10