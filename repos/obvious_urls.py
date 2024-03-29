import time
from selenium.webdriver.common.by import By
import utils.browser as browser

def get_obvious_repo_urls():
    # only gets practice and personal repo urls.
    artemis_logo = browser.sdriver.find_element(By.XPATH, '/html/body/jhi-main/div/div[1]/jhi-navbar/nav/div[1]/a')
    browser.sdriver.execute_script("arguments[0].scrollIntoView();", artemis_logo)
    time.sleep(2)
    create_practice_exercise_if_exists()
    if not click_clone_repo_button(): return {}
    personal_repo_url = get_personal_repo_url()
    practice_repo_url = get_practice_repo_url()
    urls = {}
    if personal_repo_url != '': urls['personal'] = personal_repo_url
    if practice_repo_url != '': urls['practice'] = practice_repo_url
    return urls

def get_personal_repo_url():
    repo_type_to_https()
    url = get_repo_url_from_clone_repo_dialog()
    return url

def get_practice_repo_url():
    button_exits = 0 != len(browser.sdriver.find_elements(By.XPATH, '/html/body/ngb-popover-window/div[2]/div[1]/input'))
    if not button_exits: return ''
    browser.sdriver.find_element(By.XPATH, '/html/body/ngb-popover-window/div[2]/div[1]/input').click()
    repo_type_to_https()
    url = get_repo_url_from_clone_repo_dialog()
    browser.sdriver.find_element(By.XPATH, '/html/body/ngb-popover-window/div[2]/div[1]/input').click()
    return url

def get_repo_url_from_clone_repo_dialog():
    return browser.sdriver.find_element(By.XPATH, "//*[contains(@class, 'clone-url')]").text
    
def repo_type_to_https():
    browser.sdriver.find_element(By.XPATH, "//button[contains(text(), 'HTTPS')]")
    browser.sdriver.find_element(By.CSS_SELECTOR, '#useHTTPSButton')


def click_clone_repo_button():
    button_exits = 0 != len(browser.sdriver.find_elements(By.XPATH, '/html/body/jhi-main/div/div[2]/div/jhi-course-exercise-details/div/div[1]/jhi-exercise-details-student-actions/div/div/jhi-clone-repo-button'))
    if not button_exits: return False
    browser.sdriver.find_element(By.XPATH, '/html/body/jhi-main/div/div[2]/div/jhi-course-exercise-details/div/div[1]/jhi-exercise-details-student-actions/div/div/jhi-clone-repo-button').click()
    return True

def create_practice_exercise_if_exists():
    # basically clicks 'Practice' button. So when you click 'Clone Repo' you can also select practice exercise
    if 0 != len(browser.sdriver.find_elements(By.XPATH, '/html/body/jhi-main/div/div[2]/div/jhi-course-exercise-details/div/div[1]/jhi-exercise-details-student-actions/div/div/jhi-start-practice-mode-button')):
        practice_button = browser.sdriver.find_element(By.XPATH, '/html/body/jhi-main/div/div[2]/div/jhi-course-exercise-details/div/div[1]/jhi-exercise-details-student-actions/div/div/jhi-start-practice-mode-button')
        practice_button.click()
        browser.sdriver.find_element(By.XPATH, '/html/body/ngb-popover-window/div[2]/div/div/button[1]').click()
        ## wait till practice exercise is created. For now i will just wait for certain amount of seconds
        time.sleep(10)