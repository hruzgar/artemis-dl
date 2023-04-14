from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import printPDF
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from browser import sdriver

class ArtemisExercise:
    def __init__(self, course_name, exercise_name, exercise_link):
        self.course_name = course_name
        self.exercise_name = exercise_name
        self.exercise_link = exercise_link

    def open(self):
        sdriver.get(self.exercise_link)
        try:
            WebDriverWait(sdriver, 5).until(EC.presence_of_element_located((By.XPATH, '/html/body/jhi-main/div/div[2]/div/jhi-course-exercise-details/div/jhi-header-exercise-page-with-details/div/div[1]/div[2]/span[2]/div')))
        except TimeoutException:
            print("Exercise Loading took too much time!")

    def print_exercise_to_pdf(self):
        cookie = 'jwt=' + sdriver.get_cookies()[0]['value']
        printPDF.print_Artemis_page_to_pdf(self.exercise_name, cookie=cookie)
    
    
