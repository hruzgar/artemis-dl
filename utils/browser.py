from selenium import webdriver
from utils.print import printer

class WebDriverSingleton:
    instance = None

    @staticmethod
    def get_chromedriver():
        printer('Opening Browser..')
        options = webdriver.ChromeOptions()
        options.headless = False
        options.add_argument('--no-sandbox')
        options.add_argument('--start-maximized')
        options.add_argument('--disable-popup-blocking')
        options.add_argument('--disable-gpu')
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        driver = webdriver.Chrome(options=options)
        printer('Browser successfully opened')
        return driver
    
    @classmethod
    def get_instance(cls):
        if cls.instance is None:
            cls.instance = cls.get_chromedriver()
        return cls.instance



# sdriver = get_chromedriver() # Browser Session for scraping
