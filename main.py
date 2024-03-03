import os
from snaper import Page
from pprint import pprint
from datetime import datetime
from selenium import webdriver
# TODO Make unit tests

# Config
# TODO Move to separated file
driver_path = "/home/op/Software/SeleniumChromeDriver"
list_path = "lists/sites.txt"
screenshots_path = "shots/"
browser_width = 1440
wait_in_seconds = 30

# Dir to save shots
screenshots_path = screenshots_path + datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
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

        mydriver = Page(driver, wait_in_seconds)
        mydriver.open_page(url)

        mydriver.get_width_and_height()

        mydriver.make_screenshot()

        file_path = url.split("/")[2]
        file_path = screenshots_path + file_path + '.png'

        # Save image to file
        with open(file_path, "wb") as file:
            file.write(mydriver.image)

        # driver.save_screenshot(file_path)
        print(file_path)

except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
