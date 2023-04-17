from selenium.webdriver.common.by import By
from utils.browser import sdriver
import config

def login():
    user_name = sdriver.find_element(By.NAME, "username")
    password = sdriver.find_element(By.NAME, "password")
    login_button = sdriver.find_element(By.ID, "login-button")
    user_name.send_keys(config.student_id)
    password.send_keys(config.password)
    login_button.click()

def enable_dark_mode():
    theme_selector = sdriver.find_element(By.XPATH, '//*[@id="theme-toggle"]')
    if theme_selector.get_attribute('class') != 'theme-toggle dark':
        theme_selector.click()