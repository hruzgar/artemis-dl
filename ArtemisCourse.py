from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from ArtemisExercise import ArtemisExercise
import time

class ArtemisCourse:
    def __init__(self, driver, courseName, course_link):
        self.driver = driver
        self.courseName = courseName
        self.course_link = course_link
    def scrapeExercisesToClassList(self):
        temp_exercises = self.driver.find_elements(By.CSS_SELECTOR, 'jhi-course-exercise-row')
        self.exercises = []
        for counter in range(len(temp_exercises)):
            element = temp_exercises[counter]
            tempExercise = ArtemisExercise(self.driver, ArtemisCourse.getExerciseNameFromCoursePage(element), ArtemisCourse.getExerciseLinkFromCoursePage(element))
            self.exercises.append(tempExercise)
    
    def getExerciseNameFromCoursePage(exerciseCardElement):
        return exerciseCardElement.find_element(By.XPATH, './div/div[2]/div[1]/div[2]/h4').text

    def getExerciseLinkFromCoursePage(exerciseCardElement):
        return exerciseCardElement.find_element(By.TAG_NAME, 'a').get_attribute('href')
        
    def goToFirstExercise(self):
        self.exercises[0].open_exercise_in_browser()
        self.exercises[0].print_exercise_to_pdf()
        
    
    def printAllExerciseNames(self):
        for exercise in self.exercises:
            print(exercise.exerciseName)
         
        
    def collapseAllExercises(self):
        exercise_list_elements = self.driver.find_elements(By.XPATH, '/html/body/jhi-main/div/div[2]/div/jhi-course-overview/div/div/div[2]/jhi-course-exercises/div/div[1]/div/div')
        exercise_list_elements.pop(0) # deletes search bar from element list
        print(len(exercise_list_elements))
        for t in exercise_list_elements:
            svg_element = t.find_element(By.TAG_NAME, 'svg')
            iconState = svg_element.get_attribute("data-icon")
            self.driver.execute_script("arguments[0].scrollIntoView();", svg_element)
            time.sleep(0.6)
            if iconState == 'angle-down':
                t.click()
                # time.sleep(2)
                print('clicked')
        time.sleep(5)
