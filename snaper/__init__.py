import base64
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from datetime import datetime

class Window:
    '''Browser window, its config and operations'''
    def __init__(self, driver_path, wait_in_seconds) -> None:
        self.driver_path = driver_path
        self.wait_in_seconds = wait_in_seconds

    def start_driver(self):
        options = webdriver.ChromeOptions()
        options.binary_location = self.driver_path
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

    def open_page(self):
        self._driver.get(self.url)

    def get_width_and_height(self):
        '''
        Page width and height by Google DevTools
        Method help: https://chromedevtools.github.io/devtools-protocol/tot/Page/#method-getLayoutMetrics
        '''
        try:
            metrics = self._driver.execute_cdp_cmd("Page.getLayoutMetrics", {})
            self.width = metrics["cssContentSize"]["width"]
            self.height = metrics["cssContentSize"]["height"]
        except Exception as ex:
            print(ex)

    def make_screenshot_by_devtools(self):
        '''
        Page screenshot by Google DevTools
        Method description: https://chromedevtools.github.io/devtools-protocol/tot/Page/#method-captureScreenshot
        '''
        # TODO Add some more types of screenshots
        try:
            screnshot_raw_data = self._driver.execute_cdp_cmd("Page.captureScreenshot", \
                                                           {'format': 'png', 'captureBeyondViewport': True})
            self.image_data = base64.decodebytes(bytes(screnshot_raw_data['data'], 'utf-8'))
        except Exception as ex:
            print(ex)


    def _return_current_screenshot_by_selenium(self):
        raw_image_data = self._driver.get_screenshot_as_base64()
        return base64.b64decode(raw_image_data)


    def make_one_screenshot_by_selenium(self):
        self.image_data = self._return_current_screenshot_by_selenium()


    # TODO Set of screenshots
    def make_set_of_screenshots_by_selenium(self):
        i1 = self._return_current_screenshot_by_selenium()
        # TODO Use height of window
        self._driver.execute_script("window.scrollBy(0, 1000)")
        i2 = self._return_current_screenshot_by_selenium()
        self.image_data = i2


    def save_image_to_file(self):
        '''Save image to .png file'''
        file_path = self.list.screenshots_dir + self.file_name
        with open(file_path, "wb") as file:
            file.write(self.image_data)


if __name__ == "__main__":
    pass