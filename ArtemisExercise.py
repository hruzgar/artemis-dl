import time
import printPDF
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from pathlib import Path
from browser import sdriver
from clone_repos import clone_all_repos
from obvious_repo_urls import get_obvious_repo_urls
from hidden_repo_urls import get_hidden_repo_urls
import utils
import const

class ArtemisExercise:
    def __init__(self, course_name, exercise_name, exercise_link):
        self.course_name = course_name
        self.exercise_name = exercise_name
        self.exercise_link = exercise_link
        self.exercise_download_path = const.download_dir.joinpath(utils.slugify(self.course_name)).joinpath(utils.slugify(self.exercise_name))

    def open(self):
        sdriver.get(self.exercise_link)
        try:
            WebDriverWait(sdriver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/jhi-main/div/div[2]/div/jhi-course-exercise-details/div/jhi-header-exercise-page-with-details/div/div[1]/div[2]/span[2]/div')))
        except TimeoutException:
            print("Exercise Loading took too much time!")
        time.sleep(1)

    def print_exercise_to_pdf(self):
        cookie = 'jwt=' + sdriver.get_cookies()[0]['value']
        printPDF.print_artemis_exercise_to_pdf(exercise_name=utils.slugify(self.exercise_name), exercise_download_dir=self.exercise_download_path,cookie=cookie)

    def download_exercise(self):
        self.print_exercise_to_pdf()
        self.clone_repos()

    def clone_repos(self):
        self.repo_urls = get_obvious_repo_urls() | get_hidden_repo_urls()
        clone_all_repos(repo_urls=self.repo_urls, local_download_dir=self.exercise_download_path)

    def collapse_all_parts(self):
        summary_tags = sdriver.find_elements(By.TAG_NAME, 'summary')
        for summary_tag in summary_tags:
            sdriver.execute_script("arguments[0].scrollIntoView();", summary_tag)
            time.sleep(0.7)
            summary_tag.click()


    