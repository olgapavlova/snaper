from snaper import Window, List, Page
# TODO Make unit tests

# Config
# TODO Move to separated file
driver_path = "/home/op/Software/SeleniumChromeDriver"
screenshots_path = "shots/"
browser_width = 1440
wait_in_seconds = 50
list_txt_file = "lists/sites.txt"

# Browser window
mywindow = Window(driver_path, wait_in_seconds)
mywindow.start_driver()
mywindow.set_window_width(browser_width)

# List object
mylist = List(list_txt_file, mywindow)
mylist.set_screenshot_dir(screenshots_path)

# Go through the list
try:
    for url in mylist.url_list:
        mypage = Page(mylist, wait_in_seconds, url)
        mypage.open_page()
        mypage.get_width_and_height()
        mypage.make_one_screenshot_by_selenium()
        mypage.save_image_to_file()
except Exception as ex:
    print(ex)
finally:
    mywindow.driver.close()
    mywindow.driver.quit()
