import time
from utils import config
from utils import general_utils as utils
from exercises import print_PDF, downloader
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import utils.browser as browser
from repos.clone import clone_all_repos
from repos.obvious_urls import get_obvious_repo_urls
from repos.hidden_urls import get_hidden_repo_urls
from utils.print import printer

class ArtemisExercise:

    def __init__(self, exercise_link, course_name=None, exercise_name=None):
        self.exercise_link = exercise_link
        self.course_name = course_name
        self.exercise_name = exercise_name
        self.exercise_tags = []

    def open(self):
        browser.sdriver.get(self.exercise_link)
        try:
            WebDriverWait(browser.sdriver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/jhi-main/div/div[2]/div/jhi-course-exercise-details/div/jhi-header-exercise-page-with-details/div/div[1]/div[1]/div/span')))
        except TimeoutException:
            print("Exercise Loading took too much time!")
        time.sleep(1)

        if self.exercise_name is None: self.get_exercise_name()
        if self.course_name is None: self.get_course_name()
        self.exercise_download_path = config.download_dir.joinpath(utils.slugify(self.course_name)).joinpath(
            utils.slugify(self.exercise_name))
        self.get_exercise_tags()
        if 'optional' in self.exercise_tags and 'homework' not in self.exercise_tags:
            self.exercise_download_path = config.download_dir.joinpath(utils.slugify(self.course_name)).joinpath('optional').joinpath(
            utils.slugify(self.exercise_name))

    def get_exercise_name(self):
        self.exercise_name = browser.sdriver.find_element(By.CSS_SELECTOR, '#bread-crumb-plain-3').text

    def get_course_name(self):
        self.course_name = browser.sdriver.find_element(By.CSS_SELECTOR, '#bread-crumb-plain-1').text
    
    def get_exercise_tags(self):
        self.exercise_tags = utils.get_exercise_tags_on_page()
        if 'hard' in self.exercise_tags:
            self.exercise_tags.remove('hard')
            self.exercise_difficulty = 'hard'
        elif 'medium' in self.exercise_tags:
            self.exercise_tags.remove('medium')
            self.exercise_difficulty = 'medium'
        elif 'easy' in self.exercise_tags:
            self.exercise_tags.remove('easy')
            self.exercise_difficulty = 'easy'
        else:
            self.exercise_difficulty = 'unknown'

    def print_exercise_to_pdf(self):
        cookie = 'jwt=' + browser.sdriver.get_cookies()[0]['value']
        print_PDF.print_artemis_exercise_to_pdf(exercise_name=utils.slugify(self.exercise_name), exercise_download_dir=self.exercise_download_path, cookie=cookie)

    def download_webpage(self):
        cookie = 'jwt=' + browser.sdriver.get_cookies()[0]['value']
        downloader.save_page_to_html(exercise_download_dir=self.exercise_download_path, exercise_name=utils.slugify(self.exercise_name), cookie=cookie)

    def download_exercise(self):
        if 'quiz' in self.exercise_tags:
            printer('Skipping quiz')
            return
        self.print_exercise_to_pdf()
        self.clone_repos()
        self.download_webpage()

    def clone_repos(self):
        self.repo_urls = get_obvious_repo_urls() | get_hidden_repo_urls()
        clone_all_repos(repo_urls=self.repo_urls, local_download_dir=self.exercise_download_path.joinpath('repos'))

    def collapse_all_parts(self):
        summary_tags = browser.sdriver.find_elements(By.TAG_NAME, 'details')
        for summary_tag in summary_tags:
            browser.sdriver.execute_script("arguments[0].scrollIntoView();", summary_tag)
            time.sleep(0.7)
            summary_tag.click()
