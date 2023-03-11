from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


class ArtemisMainPage:

    def __init__(self, driver: webdriver):
        self.driver = driver
        self.driver.get("https://artemis.in.tum.de/")



    def login(self, userN, passW):
        time.sleep(3)
        userName = self.driver.find_element(By.NAME, "username")
        password = self.driver.find_element(By.NAME, "password")
        loginButton = self.driver.find_element(By.ID, "login-button")
        userName.send_keys(userN)
        password.send_keys(passW)
        loginButton.click()
        time.sleep(1)

    def scrapeCoursesToList(self):
        self.courses = self.driver.find_elements(By.CSS_SELECTOR, 'jhi-overview-course-card')


    def getCourseNames(self):
        self.courseNames = []
        for course in self.courses:
            textElement = course.find_element(By.XPATH, './div/div/div/div/div[2]/h5')
            self.courseNames.append(textElement.text)
        print(type(self.courseNames))
        print(type(self.courses))
        print(self.courseNames)
        print(self.courses)