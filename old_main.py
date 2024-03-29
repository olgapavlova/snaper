from snaper import List, Page, window
# TODO Make unit tests

# Config
# TODO Move to separated file
driver_path = "/home/op/Software/SeleniumChromeDriver"
screenshots_path = "shots/"
browser_width = 1440
browser_height = 1200
wait_in_seconds = 50
list_txt_file = "lists/sites.txt"

# Browser window
mywindow = window(driver_path, wait_in_seconds)
mywindow.start_driver()
mywindow.set_window_size(browser_width, browser_height)

# List object
mylist = List(list_txt_file, mywindow)
mylist.set_screenshot_dir(screenshots_path)

# Go through the list
try:
    for url in mylist.url_list:
        mypage = Page(mylist, wait_in_seconds, url)
        mypage.open_page()
        mypage.get_width_and_height()
        mypage.make_set_of_screenshots_by_selenium()
        mypage.save_image_to_file()
except Exception as ex:
    print(ex)
finally:
    mywindow.driver.close()
    mywindow.driver.quit()
