from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from utils import config
from utils.decorators import ensure_driver, sdriver
# from utils.browser import WebDriverSingleton

# sdriver = WebDriverSingleton.get_instance()

@ensure_driver
def login():
    user_name = sdriver.find_element(By.NAME, "username")
    password = sdriver.find_element(By.NAME, "password")
    login_button = sdriver.find_element(By.ID, "login-button")
    user_name.send_keys(config.username)
    password.send_keys(config.password)
    login_button.click()

    try:
        WebDriverWait(sdriver, 6).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#account-menu')))
    except TimeoutException:
        return False
    return True

@ensure_driver
def enable_dark_mode():
    try:
        WebDriverWait(sdriver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="theme-toggle"]')))
    except TimeoutException:
        print("Course-Site Loading took too much time!")
    theme_selector = sdriver.find_element(By.XPATH, '//*[@id="theme-toggle"]')
    if theme_selector.get_attribute('class') != 'theme-toggle dark':
        theme_selector.click()
