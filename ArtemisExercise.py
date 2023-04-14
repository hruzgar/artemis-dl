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
    def __init__(self, exerciseName, exerciseLink):
        self.exerciseName = exerciseName
        self.exerciseLink = exerciseLink

    def open(self):
        sdriver.get(self.exerciseLink)
        try:
            WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, '/html/body/jhi-main/div/div[1]/jhi-navbar/nav/div[1]/a/img')))
        except TimeoutException:
            print("Exercise Loading took too much time!")

    def print_exercise_to_pdf(self):
        print("place holder")
    
    
