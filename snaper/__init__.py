import logging
from selenium import webdriver

def W(text):
    logging.warning(text)

def D(text):
    logging.debug(text)

class Task:
    '''Main task. One for module.'''

    def __init__(self, urls, breakpoints, store, options) -> None:
        D("Создаём объект Task")
        self.urls = urls
        self.breakpoints = breakpoints
        self.store = store
        self.config = Config(options)
        self.window = Window(self.config)
        self.pages = self._init_all_pages()
        D("Объект Task создан")

    def _init_all_pages(self):
        D("Инициирую все страницы")
        return [Page(self, url) for url in self.urls]

    def make_all_screenshots_by_pages(self):
        D("Запускаю постраничный сбор всех скриншотов")
        for page in self.pages: self._make_all_screenshots_for_one_page(page)
        D("Постраничный сбор скриншотов закончен")

    def _make_all_screenshots_for_one_page(self, page):
        D(f"Запускаю получение скриншотов для страницы {page.url}")
        page.make_all_screenshots()

    def save_all_screenshots_by_pages(self):
        D(f"Начинаю сохранять все скриншоты всех страниц")
        for page in self.pages: self._save_all_screenshots_for_one_page(page)

    def _save_all_screenshots_for_one_page(self, page):
        D(f"Начинаю сохранять все скриншоты для страницы {page.url}")
        page.save_all_screenshots()

class Config:
    '''Configuration for all technical behaviours.'''

    def __init__(self, options) -> None:
        D("Создаём конфигурационный объект Config в объекте Task")
        self.driver_path = options['driver_path']
        self.driver_delay = options['driver_delay']
        self.screenshot_type = options['screenshot_type']
        D("Объект Config создан")


class Page:
    '''Pages to be screenshoted.'''

    def __init__(self, task, url) -> None:
        D(f"Создаём страницу с URL {url}")
        self.task = task
        self.url = url
        self.window = self.task.window  # TODO Depends on order of attribute, better to fix
        self.screenshots = self._init_all_screenshots_by_breakpoints()
        D(f"Страница с URL {self.url} создана")

    def _init_all_screenshots_by_breakpoints(self):
        D(f"Инициирую все объекты скриншотов для страницы {self.url}")
        screenshots = [self._init_screenshot(breakpoint) for breakpoint in self.task.breakpoints]
        return screenshots

    def _init_screenshot(self, breakpoint):
        D(f"...брейкпоинт {breakpoint}")
        return Screenshot(self, breakpoint)

    def make_all_screenshots(self):
        D(f"Собираю все скриншоты со страницы {self.url}")
        self._open_page_in_window()
        for screenshot in self.screenshots: self._make_screenshot(screenshot)

    def _open_page_in_window(self):
        D(f"Открываю в браузере страницу {self.url}")

    def _make_screenshot(self, screenshot):
        D(f"Делаю скриншот {screenshot.breakpoint} для страницы {self.url}")

    def save_all_screenshots(self):
        D(f"Сохраняю все скриншоты со страницы {self.url}")
        for screeenshot in self.screenshots: self._save_screenshot(screeenshot)

    def _save_screenshot(self, screenshot):
        D(f"Сохраняю скриншот {screenshot.breakpoint} для страницы {self.url}")
        screenshot.save()



class Screenshot:
    '''Some screenshots for each page.'''

    def __init__(self, page, breakpoint) -> None:
        D(f"В странице {page.url} инициируем скриншот с шириной {breakpoint}")
        self.page = page
        self.breakpoint = breakpoint
        self.name = self._init_name_for_store()
        self.window = self.page.window
        D(f"Скриншот с шириной {self.breakpoint} в странице {self.page.url} создан")
        # TODO self.image

    def _init_name_for_store(self):
        breakpoint = str(self.breakpoint)
        url = self.page.url.split("/")[2]
        extension = '.png'
        name = breakpoint + '_' + url + extension
        D(f".....имя файла {name}")
        return name

    def make_image(self):
        W(f"Начинаю делать скриншот")
        self._make_image_first()

    def _make_image_first(self):
        W(f"Делаю скриншот первой страницы")

    def _make_image_full(self):
        W(f"Делаю скриншот по схеме full")

    def _make_image_stepbystep(self):
        W(f"Делаю скриншот по схеме stepbystep")

    def _make_image_updown(self):
        W(f"Делаю скриншот по схеме updown")

    def save(self):
        W(f"Сохраняю скриншот")
        self._merge_image()
        self._write_to_file()

    def _merge_image(self):
        W(f"Объединяю части скриншота в одно изображение")

    def _write_to_file(self):
        W(f"Записываю в файл {self.name} в каталоге {self.page.task.store}")


class Window:
    '''Enhancement for driver class. Some size, etc.'''

    def __init__(self, config) -> None:
        D("Создаём окно")
        # TODO self.width
        # TODO self.height
        self.driver = Driver(config)
        D("Окно создано")


class Driver:
    '''Technical class, no reason to be seen outside.'''

    def __init__(self, config) -> None:
        D("Создаём драйвер")
        self.path = config.driver_path
        self.driver = self.start()
        D("Драйвер создан")

    def start(self):
        '''Start physical browser driver in OS.'''
        D("Стартуем драйвер")
        options = webdriver.ChromeOptions()
        options.binary_location = self.path
        driver = webdriver.Chrome()
        D("Драйвер стартовал")
        return driver

    def stop(self):
        '''Placeholder to stop driver.'''
        pass