import base64
import os
from datetime import datetime
from selenium import webdriver
# TODO Make unit tests

# Config
# TODO Move to separated file
driver_path = "/home/op/Software/SeleniumChromeDriver"
list_path = "lists/UX Companies.txt"
screenshots_path = "shots/"
browser_width = 1440
wait_in_seconds = 5

# Dir to save shots
screenshots_path = screenshots_path + datetime.now().strftime("%Y-%M-%d-%H-%M")
os.mkdir(screenshots_path)
screenshots_path = screenshots_path + "/"
# TODO Add check if path exists (however, it is temp decision)

# Init webdriver
options = webdriver.ChromeOptions()
options.binary_location = driver_path
driver = webdriver.Chrome()

# Change browser width
browser_height = driver.get_window_size()['height']
driver.set_window_size(width=browser_width, height=browser_height)

# Read list of URLs
url_list = []
with open(list_path, 'r') as list:
    for line in list:
        url_list.append(line.rstrip('\n'))

# Go through the list
try:
    for url in url_list:
        driver.get(url)
        # TODO Replace waiting by explicit one
        driver.implicitly_wait(wait_in_seconds)

        # Page heigth by Google DevTools
        try:
            metrics = driver.execute_cdp_cmd("Page.getLayoutMetrics", {})
            page_heigth = metrics['contentSize']['height']
            # print(page_heigth)
        except Exception as mex:
            print(mex)

        # Page screenshot by Google DevTools
        try:
            screnshot_by_devtools = driver.execute_cdp_cmd("Page.captureScreenshot", \
                                                           {'format': 'png', 'captureBeyondViewport': True})
            # print(type(screnshot_by_devtools['data']))
        except Exception as smex:
            print(smex)

        file_path = url.split("/")[2]
        file_path = screenshots_path + file_path + '.png'

        # Save image to file
        image_data = base64.decodebytes(bytes(screnshot_by_devtools['data'], 'utf-8'))
        with open(file_path, "wb") as file:
            file.write(image_data)

        # driver.save_screenshot(file_path)
        print(file_path)

except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
