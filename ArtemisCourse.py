import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from ArtemisExercise import ArtemisExercise
from browser import sdriver

class ArtemisCourse:
    def __init__(self, course_name, course_link):
        self.course_name = course_name
        self.course_link = course_link

    def open(self):
        sdriver.get(self.course_link)
        try:
            WebDriverWait(sdriver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/jhi-main/div/div[2]/div/jhi-course-overview/div/div/div[2]/jhi-course-exercises/div/div[1]/div/div[1]/div/button')))
        except TimeoutException:
            print("Course-Site Loading took too much time!")
        self.collapse_all_exercises()
        self.scrape_exercises_to_class_list()

    def scrape_exercises_to_class_list(self):
        temp_exercises = sdriver.find_elements(By.CSS_SELECTOR, 'jhi-course-exercise-row')
        self.exercises = []
        for counter in range(len(temp_exercises)):
            exercise_card_element = temp_exercises[counter]
            exercise_name = exercise_card_element.find_element(By.XPATH, './div/div[2]/div[1]/div[2]/h4').text
            exercise_link = exercise_card_element.find_element(By.TAG_NAME, 'a').get_attribute('href')
            temp_exercise = ArtemisExercise(self.course_name, exercise_name, exercise_link)
            self.exercises.append(temp_exercise)
    
    def download_one_exercise(self):
        exercise_num = 9
        self.exercises[exercise_num].open()
        self.exercises[exercise_num].download_exercise()

    def download_all_exercises(self):
        for exercise in self.exercises:
            exercise.open()
            exercise.download_exercise()
        
    def collapse_all_exercises(self):
        exercise_list_elements = sdriver.find_elements(By.XPATH, '/html/body/jhi-main/div/div[2]/div/jhi-course-overview/div/div/div[2]/jhi-course-exercises/div/div[1]/div/div')
        exercise_list_elements.pop(0) # deletes search bar from element list
        print(len(exercise_list_elements))
        for t in exercise_list_elements:
            svg_element = t.find_element(By.TAG_NAME, 'svg')
            icon_state = svg_element.get_attribute("data-icon")
            sdriver.execute_script("arguments[0].scrollIntoView();", svg_element)
            time.sleep(0.7)
            if icon_state == 'angle-down':
                t.click()
                # time.sleep(2)
                print('clicked')
