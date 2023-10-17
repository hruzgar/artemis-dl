import os
from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from utils.print import printer

sdriver = None

# # Decorator for all functions, which use the WebDriver. It ensures, that the WebDriver is only opened once and then reused.
# def ensure_driver(func):
#     def wrapper(*args, **kwargs):
#         # if not hasattr(ensure_driver, "sdriver"):
#         #     ensure_driver._driver = WebDriverSingleton.get_instance()
#         # if not hasattr(ensure_driver, "sdriver"):
#         #     ensure_driver.sdriver = WebDriverSingleton.get_instance()
#         global sdriver
#         if globals()["sdriver"] is None:
#             globals()["sdriver"] = WebDriverSingleton.get_instance()
#         return func(*args, **kwargs)
#     return wrapper

class WebDriverSingleton:
    instance = None

    @staticmethod
    def get_edgedriver():
        printer('Opening Browser..')
        options = webdriver.EdgeOptions()
        # options.headless = True # doesnt work anymore in new chrome/edge version
        options.add_argument('--no-sandbox')
        options.add_argument('--start-maximized')
        options.add_argument('--disable-popup-blocking')
        options.add_argument('--disable-gpu')
        options.add_argument("--headless=new")
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        driver = webdriver.Edge(options=options, service=EdgeService(EdgeChromiumDriverManager().install()))
        # driver = webdriver.Chrome(options=options)
        printer('Browser successfully opened')
        return driver

    @staticmethod
    def get_chromedriver():
        printer('Opening Browser..')
        options = webdriver.ChromeOptions()
        # options.headless = True # doesnt work anymore in new chrome/edge version
        options.add_argument('--no-sandbox')
        options.add_argument('--start-maximized')
        options.add_argument('--disable-popup-blocking')
        options.add_argument('--disable-gpu')
        options.add_argument("--headless=new")
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
        # driver = webdriver.Chrome(options=options)
        printer('Browser successfully opened')
        return driver
    
    @classmethod
    def get_instance(cls):
        if cls.instance is None:
            if os.name == 'nt':
                cls.instance = cls.get_edgedriver()
            else:
                cls.instance = cls.get_chromedriver()
        global sdriver
        # if globals()["sdriver"] is None:
        globals()["sdriver"] = cls.instance
        return cls.instance