import logging
from selenium import webdriver

def L(text):
    logging.warning(text)

class Task:
    '''Main task. One for module.'''

    def __init__(self, urls, breakpoints, store, options) -> None:
        L("Создаём объект Task")
        self.urls = urls
        self.breakpoints = breakpoints
        self.store = store
        self.config = Config(options)
        self.window = Window(self.config)
        self.pages = [Page(url) for url in self.urls]
        L("Объект Task создан")

class Config:
    '''Configuration for all technical behaviours.'''

    def __init__(self, options) -> None:
        L("Создаём конфигурационный объект Config в объекте Task")
        self.driver_path = options['driver_path']
        self.driver_delay = options['driver_delay']
        self.screenshot_type = options['screenshot_type']
        L("Объект Config создан")


class Page:
    '''Pages to be screenshoted.'''

    def __init__(self, url) -> None:
        L(f"Создаём страницу с URL {url}")
        self.url = url
        L(f"Страница с URL {self.url} создана")
        # TODO self.screenshots
        # TODO self.window


class Screenshot:
    '''Some screenshots for each page.'''

    def __init__(self, breakpoint) -> None:
        L(f"В странице !!! инициируем скриншот с шириной {breakpoint}")
        self.breakpoint = breakpoint
        # TODO self.image
        # TODO self.name
        # TODO self.window
        L(f"Скриншот с шириной {self.breakpoint} в странице !!! создан")


class Window:
    '''Enhancement for driver class. Some size, etc.'''

    def __init__(self, config) -> None:
        L("Создаём окно")
        # TODO self.width
        # TODO self.height
        self.driver = Driver(config)
        L("Окно создано")


class Driver:
    '''Technical class, no reason to be seen outside.'''

    def __init__(self, config) -> None:
        L("Создаём драйвер")
        self.path = config.driver_path
        self.driver = self.start()
        L("Драйвер создан")

    def start(self):
        '''Start physical browser driver in OS.'''
        L("Стартуем драйвер")
        options = webdriver.ChromeOptions()
        options.binary_location = self.path
        driver = webdriver.Chrome()
        L("Драйвер стартовал")
        return driver

    def stop(self):
        '''Placeholder to stop driver.'''
        pass