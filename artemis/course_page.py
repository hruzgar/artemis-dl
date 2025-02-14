import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from artemis.exercise_page import ArtemisExercise
import utils.browser as browser
from utils.print import printer

class ArtemisCourse:

    def __init__(self, course_link, course_name=None):
        self.course_name = course_name
        self.course_link = course_link

    def open(self):
        printer(f"Opening Course-Page")
        browser.sdriver.get(self.course_link)
        try:
            WebDriverWait(browser.sdriver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/jhi-app/div/div[2]/div/jhi-course-overview/div[1]/div/mat-sidenav-container/mat-sidenav-content/div[2]/jhi-course-exercises/div/div[1]/jhi-sidebar/div/div/div/div/div[2]/jhi-sidebar-accordion/div/div[1]')))
        except TimeoutException:
            print("Course-Site Loading took too much time!")
        time.sleep(1)
        if self.course_name is None: self.get_course_name()
        printer(f'Course-Page "{self.course_name}" opened')
        self.collapse_all_exercises_old()
        # self.collapse_all_exercises_new()
        # self.scrape_exercises_to_class_list() (deprecated) (collecting doesn't work anymore with the newest Artemis version)
        
        self.download_all_exercises_one_by_one()
    
    def get_course_name(self):
        self.course_name = browser.sdriver.find_element(By.CSS_SELECTOR, '#bread-crumb-plain-1').text



    #### (Deprecated because of new Artemis version doesnt show links from exercises anymore)
    # def scrape_exercises_to_class_list(self):
    #     temp_exercises = browser.sdriver.find_elements(By.CSS_SELECTOR, '#test-accordion-item-content > div')
    #     self.exercises = []
    #     for counter in range(len(temp_exercises)):
    #         exercise_card_element = temp_exercises[counter]
    #         exercise_name = exercise_card_element.find_element(By.XPATH, './jhi-medium-sidebar-card/div/jhi-sidebar-card-item/div/div[1]/span[1]').text
    #         exercise_link = exercise_card_element.find_element(By.TAG_NAME, 'a').get_attribute('href')
    #         temp_exercise = ArtemisExercise(exercise_link=exercise_link, course_name=self.course_name, exercise_name=exercise_name)
    #         printer(f"Exercise Name: {exercise_name}, link: {exercise_link}")
    #         self.exercises.append(temp_exercise)
    
    def download_one_exercise(self):
        exercise_num = 9
        self.exercises[exercise_num].open()
        self.exercises[exercise_num].download_exercise()

    def download_all_exercises_one_by_one(self):
        temp_exercises = browser.sdriver.find_elements(By.CSS_SELECTOR, '#test-accordion-item-content > div')
        self.exercises = []
        print()
        for counter in range(25, len(temp_exercises)):
            exercise_card_element = temp_exercises[counter]
            exercise_name = exercise_card_element.find_element(By.XPATH, './jhi-medium-sidebar-card/div/jhi-sidebar-card-item/div/div[1]/span[1]').text
            exercise_card_element.click()
            current_exercise = ArtemisExercise(course_name=self.course_name, exercise_name=exercise_name)

            printer(f'Downloading Exercise "{exercise_name}" ({counter + 1}/{len(temp_exercises)})')
            start = time.time()
            current_exercise.open()
            current_exercise.download_exercise()
            end = time.time()
            elapsed_time = round(end - start)
            printer(f'Successful! Downloaded in {elapsed_time} seconds\n')

            self.exercises.append(current_exercise)

    def download_all_exercises(self):
        print()
        for counter in range(len(self.exercises)):
            printer(f'{counter + 1}/{len(self.exercises)}: Downloading Exercise "{self.exercises[counter].exercise_name}"')
            start = time.time()
            self.exercises[counter].open()
            self.exercises[counter].collapse_all_parts()
            self.exercises[counter].download_exercise()
            end = time.time()
            elapsed_time = round(end - start)
            printer(f'Successful! Downloaded in {elapsed_time} seconds\n')
        
    def collapse_all_exercises_old(self):
        printer("Collapsing exercises on course-page")
        exercise_list_elements = browser.sdriver.find_elements(By.XPATH, '//*[@id="test-accordion-item-container-3"]')
        # exercise_list_elements.pop(0) # deletes search bar from element list
        for t in exercise_list_elements:
            svg_element = t.find_element(By.TAG_NAME, 'svg')
            icon_state = svg_element.get_attribute("data-icon")
            browser.sdriver.execute_script("arguments[0].scrollIntoView();", svg_element)
            time.sleep(1)
            if icon_state == 'chevron-right':
                t.click()

    def collapse_all_exercises_new(self):
        elements = browser.sdriver.find_elements(By.CSS_SELECTOR, '.rotate-icon.chevron-position')

        for element in elements:
            if 'rotated' not in element.get_attribute('class').split():
                browser.sdriver.execute_script("arguments[0].scrollIntoView();", element)
                time.sleep(1)
                element.click()
                time.sleep(2)
