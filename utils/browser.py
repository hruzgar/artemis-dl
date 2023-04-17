from selenium import webdriver

def get_chromedriver():
    options = webdriver.ChromeOptions()
    options.headless = False
    options.add_argument('--no-sandbox')
    options.add_argument('--start-maximized')
    options.add_argument('--disable-popup-blocking')
    options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(options=options)
    return driver

sdriver = get_chromedriver() # Browser Session for scraping
