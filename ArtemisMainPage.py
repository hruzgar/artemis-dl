from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from ArtemisCourse import ArtemisCourse
import time
from browser import sdriver

class ArtemisMainPage:

    def __init__(self):
        sdriver.get("https://artemis.in.tum.de/")

    def login(userN, passW):
        userName = sdriver.find_element(By.NAME, "username")
        password = sdriver.find_element(By.NAME, "password")
        loginButton = sdriver.find_element(By.ID, "login-button")
        userName.send_keys(userN)
        password.send_keys(passW)
        loginButton.click()

    def scrapeCoursesToClassList(self):
        temp_courses = sdriver.find_elements(By.CSS_SELECTOR, 'jhi-overview-course-card')
        self.courses = []
        for counter in range(len(temp_courses)):
            course_card_element = temp_courses[counter]
            course_name = course_card_element.find_element(By.XPATH, './div/div/div/div/div[2]/h5').text
            course_link = course_card_element.find_element(By.XPATH, './div/div[1]/a').get_attribute('href') 
            tempClass = ArtemisCourse(course_name, course_link)
            self.courses.append(tempClass)
    
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
