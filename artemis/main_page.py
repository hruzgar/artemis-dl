from selenium.webdriver.common.by import By
from . course_page import ArtemisCourse
from utils.browser import ensure_driver
import utils.browser as browser

class ArtemisMainPage:
    @ensure_driver
    def scrape_courses_to_class_list(self):
        temp_courses = browser.sdriver.find_elements(By.CSS_SELECTOR, 'jhi-overview-course-card')
        self.courses = []
        for counter in range(len(temp_courses)):
            course_card_element = temp_courses[counter]
            course_name = course_card_element.find_element(By.XPATH, './div/div/div/div/div[2]/h5').text
            course_link = course_card_element.find_element(By.XPATH, './div/div[1]/a').get_attribute('href') 
            tempClass = ArtemisCourse(course_name, course_link)
            self.courses.append(tempClass)
    
    def enterCourses(self, first, last):
        for num in range(first, last):
            self.courses[num].open()
            self.courses[num].download_one_exercise()
            # self.courses[num].printAllExerciseNames()
            # self.courses[num].goToFirstExercise()

    def enterAllCourses(self):
        self.enterCourses(0, len(self.courses))
