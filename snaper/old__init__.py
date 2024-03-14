import base64
import os
from selenium import webdriver
from datetime import datetime

class Window:
    '''Browser window, its config and operations'''
    def __init__(self, driver_path, wait_in_seconds) -> None:
        self.driver_path = driver_path
        self.wait_in_seconds = wait_in_seconds

    def start_driver(self):
        options = webdriver.ChromeOptions()
        options.binary_location = self.driver_path
        # TODO Scrollbar does not work properly, fix it
        options.add_argument("--hide-scrollbars")
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(self.wait_in_seconds)
        # TODO Does it work here? Replace waiting by explicit one

    def set_window_size(self, width, height):
        # height = self.driver.get_window_size()['height']
        self.driver.set_window_size(width=width, height=height)

    def set_window_width_keep_height(self, width):
        height = self.driver.get_window_size()['height']
        self.set_window_size(width, height)

class List:
    '''List of URLs to make screenshots'''
    def __init__(self, txt_file, mywindow) -> None:
        self.txt_file = txt_file
        self.url_list = self._set_url_list()
        self.driver = mywindow.driver

    def _set_url_list(self):
        url_list = []
        with open(self.txt_file, 'r') as list:
            for line in list:
                url_list.append(line.rstrip('\n'))
        return url_list

    def set_screenshot_dir(self, screenshots_path):
        full_screenshots_path = screenshots_path + datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
        try:
            os.mkdir(full_screenshots_path)
        except Exception as ex:
            print(ex)

        self.screenshots_dir = full_screenshots_path + "/"
        # TODO Add check if path exists (however, it is temp decision)


class Page:
    '''One page from the list'''
    def __init__(self, list, wait_in_seconds, url) -> None:
        self.list = list  # TODO Divorce with List class to use separately
        self._driver = list.driver
        self.url = url
        self.file_name = self.url.split("/")[2] + ".png"



    def save_image_to_file(self):
        '''Save image to .png file'''
        file_path = self.list.screenshots_dir + self.file_name
        with open(file_path, "wb") as file:
            file.write(self.image_data)


if __name__ == "__main__":
    pass