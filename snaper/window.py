import base64
import time
import io
from selenium import webdriver
from PIL import Image

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

   # TODO Where to move? Nothing to do here
    def create_image_object_from_binary_source(self, binary_source):
        return Image.open(io.BytesIO(binary_source))

    def screenshot_full_page(self):
        '''
        Page screenshot by Google DevTools
        Method description: https://chromedevtools.github.io/devtools-protocol/tot/Page/#method-captureScreenshot
        '''
        try:
            screnshot_raw_data = self.driver.execute_cdp_cmd("Page.captureScreenshot", \
                                                        {'format': 'png', 'captureBeyondViewport': True})
            decoded = base64.decodebytes(bytes(screnshot_raw_data['data'], 'utf-8'))
            result = self.create_image_object_from_binary_source(decoded)
            return result
        except Exception as ex:
            print(ex)

    def screenshot_one_page(self):
        raw_image_data = self.driver.get_screenshot_as_base64()
        binary_source = base64.b64decode(raw_image_data)
        result = self.create_image_object_from_binary_source(binary_source)
        return result

    def scroll_page(self, height):
        self.driver.execute_script(f"window.scrollBy(0, {height})")
        return

    def screenshots_step_by_step(self):
        size = self.get_page_width_and_height()
        height_step = self.count_screen_heigth() - 400
        result = []
        for i in range(round(size["height"]/height_step + 1)):
            img = self.screenshot_one_page()
            img = self.crop_image_object_from_top_and_bottom(img, 200, 200)
            result.append(img)
            self.scroll_page(height_step)
            time.sleep(5)
        return result

    def count_screen_heigth(self):
        im = self.screenshot_one_page()
        return im.height

    def save_image_to_file(self, image, file):
        image.save(file)

    def crop_image_object_from_top_and_bottom(self, image, top, bottom):
        stripe = (0, top, image.width, image.height-bottom)
        image_cropped = image.crop(stripe)
        return image_cropped


if __name__ == "__main__":

    test_url = "https://www.subject-7.com/unified-testing/"
    test_screenshot_dir = "test_screenshot_dir/"

    window = Window(10)
    assert window.wait_in_seconds == 10

    window.start_driver()
    window.open_page(test_url)
    print(window.get_page_width_and_height())
    img_full = window.screenshot_full_page()
    # img_full = window.create_image_object_from_binary_source(img_full)
    window.save_image_to_file(img_full, f"{test_screenshot_dir}img_full.png")

    window.scroll_page(1500)
    img_one = window.screenshot_one_page()
    window.save_image_to_file(img_one, f"{test_screenshot_dir}img_one.png")

    window.scroll_page(-1500)
    img_set = window.screenshots_step_by_step()
    print(len(img_set))
    for (num, img) in enumerate(img_set):
        window.save_image_to_file(img, f"{test_screenshot_dir}img_{num}.png")

    print(window.count_screen_heigth())
