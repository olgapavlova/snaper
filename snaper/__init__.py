import base64

# TODO Make List class
# TODO Make Window class

class Page:

    def __init__(self, driver, wait_in_seconds) -> None:
        self._driver = driver
        self._driver.implicitly_wait(wait_in_seconds)
        # TODO Replace waiting by explicit one

    def open_page(self, url):
        self.url = url
        self._driver.get(url)


    def get_width_and_height(self):
        '''Page width and height by Google DevTools'''
        try:
            metrics = self._driver.execute_cdp_cmd("Page.getLayoutMetrics", {})
            self.width = metrics["contentSize"]["width"]
            self.height = metrics["contentSize"]["height"]
        except Exception as ex:
            print(ex)

    def make_screenshot(self):
        '''Page screenshot by Google DevTools'''
        # TODO Add some more types of screenshots
        try:
            screnshot_raw_data = self._driver.execute_cdp_cmd("Page.captureScreenshot", \
                                                           {'format': 'png', 'captureBeyondViewport': True})
            self.image = base64.decodebytes(bytes(screnshot_raw_data['data'], 'utf-8'))
        except Exception as ex:
            print(ex)


if __name__ == "__main__":
    pass