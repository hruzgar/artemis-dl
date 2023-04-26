import time
from utils import printPDF, utils
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from utils.browser import sdriver
from git_repos.clone_repos import clone_all_repos
from git_repos.obvious_repo_urls import get_obvious_repo_urls
from git_repos.hidden_repo_urls import get_hidden_repo_urls
import config
from utils.utils import printer

class ArtemisExercise:
    def __init__(self, exercise_link, course_name=None, exercise_name=None):
        self.exercise_link = exercise_link
        self.course_name = course_name
        self.exercise_name = exercise_name

    def open(self):
        sdriver.get(self.exercise_link)
        try:
            WebDriverWait(sdriver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/jhi-main/div/div[2]/div/jhi-course-exercise-details/div/jhi-header-exercise-page-with-details/div/div[1]/div[2]/span[2]/div')))
        except TimeoutException:
            print("Exercise Loading took too much time!")
        time.sleep(1)

        if self.exercise_name is None: self.get_exercise_name
        if self.get_course_name is None: self.get_course_name
        self.exercise_download_path = config.download_dir.joinpath(utils.slugify(self.course_name)).joinpath(
            utils.slugify(self.exercise_name))

    def get_exercise_name(self):
        self.exercise_name = sdriver.find_element(By.CSS_SELECTOR, '#bread-crumb-plain-3').text

    def get_course_name(self):
        self.course_name = sdriver.find_element(By.CSS_SELECTOR, '#bread-crumb-plain-1').text


    def print_exercise_to_pdf(self):
        cookie = 'jwt=' + sdriver.get_cookies()[0]['value']
        printPDF.print_artemis_exercise_to_pdf(exercise_name=utils.slugify(self.exercise_name), exercise_download_dir=self.exercise_download_path, cookie=cookie)

    def download_exercise(self):
        self.print_exercise_to_pdf()
        self.clone_repos()

    def clone_repos(self):
        self.repo_urls = get_obvious_repo_urls() | get_hidden_repo_urls()
        clone_all_repos(repo_urls=self.repo_urls, local_download_dir=self.exercise_download_path)

    def collapse_all_parts(self):
        summary_tags = sdriver.find_elements(By.TAG_NAME, 'details')
        for summary_tag in summary_tags:
            sdriver.execute_script("arguments[0].scrollIntoView();", summary_tag)
            time.sleep(0.7)
            summary_tag.click()


    