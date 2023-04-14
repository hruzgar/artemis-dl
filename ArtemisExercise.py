from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import printPDF
import time

class ArtemisExercise:
    def __init__(self, driver, exerciseName, exerciseLink):
        self.driver = driver
        self.exerciseName = exerciseName
        self.exerciseLink = exerciseLink

    def open_exercise_in_browser(self):
        self.driver.get(self.exerciseLink)

    def print_exercise_to_pdf(self):
        print("place holder")
    
    
