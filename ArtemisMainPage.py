from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from ArtemisCourse import ArtemisCourse
import time

class ArtemisMainPage:

    def __init__(self, driver: webdriver):
        self.driver = driver
        self.driver.get("https://artemis.in.tum.de/")

    def login(self, userN, passW):
        userName = self.driver.find_element(By.NAME, "username")
        password = self.driver.find_element(By.NAME, "password")
        loginButton = self.driver.find_element(By.ID, "login-button")
        userName.send_keys(userN)
        password.send_keys(passW)
        loginButton.click()

    def scrapeCoursesToClassList(self):
        temp_courses = self.driver.find_elements(By.CSS_SELECTOR, 'jhi-overview-course-card')
        self.courses = []
        for counter in range(len(temp_courses)):
            element = temp_courses[counter]
            tempClass = ArtemisCourse(self.driver, ArtemisMainPage.get_course_name_from_MainPage(element), ArtemisMainPage.get_course_link_from_MainPage(element))
            self.courses.append(tempClass)

    def get_course_name_from_MainPage(course_card_element):
        return course_card_element.find_element(By.XPATH, './div/div/div/div/div[2]/h5').text

    def get_course_link_from_MainPage(course_card_element):
        return course_card_element.find_element(By.XPATH, './div/div[1]/a').get_attribute('href')
    
    def enterCourses(self, first, last):
        for num in range(first, last):
            self.driver.get(self.courses[num].course_link)
            time.sleep(2)
            self.courses[num].collapseAllExercises()
            self.courses[num].scrapeExercisesToClassList()
            self.courses[num].printAllExerciseNames()
            self.courses[num].goToFirstExercise()


    def enterAllCourses(self):
        self.enterCourses(0, len(self.courses))
