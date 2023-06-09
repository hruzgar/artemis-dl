from selenium import webdriver
from utils.utils import printer

def get_chromedriver():
    printer('Opening Browser..')
    options = webdriver.ChromeOptions()
    options.headless = True
    options.add_argument('--no-sandbox')
    options.add_argument('--start-maximized')
    options.add_argument('--disable-popup-blocking')
    options.add_argument('--disable-gpu')
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(options=options)
    printer('Browser successfully opened')
    return driver


sdriver = get_chromedriver() # Browser Session for scraping
