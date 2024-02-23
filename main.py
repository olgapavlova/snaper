from selenium import webdriver
# TODO Make unit tests

# Config
# TODO Move to separated file
driver_path = "/home/op/Software/SeleniumChromeDriver"
list_path = "sites.txt"
screenshots_path = "shots/"

# Init webdriver
options = webdriver.ChromeOptions()
options.binary_location = driver_path
driver = webdriver.Chrome()

# Read list of URLs
url_list = []
with open(list_path, 'r') as list:
    for line in list:
        url_list.append(line.rstrip('\n'))

# Go through the list
try:
    for url in url_list:
        driver.get(url)
        driver.implicitly_wait(5)
        # TODO Replace waiting by explicit one
        file_path = url.replace("/", "").replace(":", "")
        file_path = screenshots_path + file_path + '.png'
        driver.save_screenshot(file_path)
        print(file_path)

except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()