from snaper import Config, Task

options_for_snaper = {
    'driver_path': '/home/op/Software/SeleniumChromeDriver',
    'driver_delay': '10',
    'screenshot_type': 'first',
}

mytask = Task(urls=['https://www.producthunt.com', 'https://www.microsoft.com'], breakpoints=[1024, 1440], store='shots/', options=options_for_snaper)
mytask.make_all_screenshots_by_pages()
mytask.save_all_screenshots_by_pages()