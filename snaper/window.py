import base64
import time
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

    def open_page(self, url):
        self.driver.get(url)

    def get_page_width_and_height(self):
        '''
        Page (not window) width and height by Google DevTools
        Method help: https://chromedevtools.github.io/devtools-protocol/tot/Page/#method-getLayoutMetrics
        '''
        try:
            metrics = self.driver.execute_cdp_cmd("Page.getLayoutMetrics", {})
            width = metrics["cssContentSize"]["width"]
            height = metrics["cssContentSize"]["height"]
            return {"width": width, "height": height}
        except Exception as ex:
            print(ex)

    def screenshot_full_page(self):
        '''
        Page screenshot by Google DevTools
        Method description: https://chromedevtools.github.io/devtools-protocol/tot/Page/#method-captureScreenshot
        '''
        try:
            screnshot_raw_data = self.driver.execute_cdp_cmd("Page.captureScreenshot", \
                                                        {'format': 'png', 'captureBeyondViewport': True})
            result = base64.decodebytes(bytes(screnshot_raw_data['data'], 'utf-8'))
            return result
        except Exception as ex:
            print(ex)

    def screenshot_one_page(self):
        raw_image_data = self.driver.get_screenshot_as_base64()
        result = base64.b64decode(raw_image_data)
        return result

    def scroll_page(self, height):
        self.driver.execute_script(f"window.scrollBy(0, {height})")
        return

    def screenshots_step_by_step(self):
        size = self.get_page_width_and_height()
        result = []
        for i in range(round(size["height"]/700 + 1)):
            img = self.screenshot_one_page()
            result.append(img)
            self.scroll_page(700)
        return result


if __name__ == "__main__":

    test_url = "https://www.producthunt.com"

    window = Window(10)
    assert window.wait_in_seconds == 10

    window.start_driver()
    window.open_page(test_url)
    print(window.get_page_width_and_height())
    img_full = window.screenshot_full_page()
    window.scroll_page(1500)
    img_one = window.screenshot_one_page()
    window.scroll_page(-1500)
    img_set = window.screenshots_step_by_step()
    print(len(img_set))
