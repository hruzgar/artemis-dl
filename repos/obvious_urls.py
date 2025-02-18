import time
from selenium.webdriver.common.by import By
import utils.browser as browser


def get_obvious_repo_urls():
    # only gets practice and personal repo urls.
    artemis_logo = browser.sdriver.find_element(By.XPATH, '//*[@id="page-wrapper"]/div[1]/jhi-navbar/nav/div[1]/a/div[1]')
    browser.sdriver.execute_script("arguments[0].scrollIntoView();", artemis_logo)
    time.sleep(2)
    resume_practice_in_exercise_if_button_exists()
    create_practice_exercise_if_button_still_exists()
    if not click_CODE_button(): return {}
    personal_repo_url = get_personal_repo_url()
    practice_repo_url = get_practice_repo_url()
    if not click_CODE_button(): return {}
    time.sleep(1)
    urls = {}
    if personal_repo_url != '': urls['personal'] = personal_repo_url
    if practice_repo_url != '': urls['practice'] = practice_repo_url
    return urls

def get_personal_repo_url():
    repo_type_to_https()
    url = get_repo_url_from_clone_repo_dialog()
    return url

def get_practice_repo_url():
    practicemode_selector_XPATH = '/html/body/ngb-popover-window/div[2]/div[1]/input'
    button_exits = 0 != len(browser.sdriver.find_elements(By.XPATH, practicemode_selector_XPATH))
    if not button_exits: return ''
    browser.sdriver.find_element(By.XPATH, practicemode_selector_XPATH).click()
    repo_type_to_https()
    url = get_repo_url_from_clone_repo_dialog()
    # browser.sdriver.find_element(By.XPATH, practicemode_selector_XPATH).click()
    return url

def get_repo_url_from_clone_repo_dialog():
    return browser.sdriver.find_element(By.XPATH, "//*[contains(@class, 'clone-url')]").text
    
def repo_type_to_https():
    browser.sdriver.find_element(By.XPATH, "//button[contains(text(), 'HTTPS')]").click()
    browser.sdriver.find_element(By.CSS_SELECTOR, '#useHTTPSButton').click()


def click_CODE_button():
    CODE_button = '//button[contains(., "Code")]'
    button_exits = 0 != len(browser.sdriver.find_elements(By.XPATH, CODE_button))
    if not button_exits: return False
    # browser.sdriver.find_element(By.XPATH, CODE_button).click()
    browser.sdriver.execute_script("arguments[0].click();", browser.sdriver.find_element(By.XPATH, CODE_button))

    return True

def create_practice_exercise_if_button_still_exists():
    # basically clicks 'Practice' button. So when you click 'Clone Repo' you can also select practice exercise
    practice_button_xpath = '//button[contains(., "Practice")]'
    if 0 != len(browser.sdriver.find_elements(By.XPATH, practice_button_xpath)):
        practice_button = browser.sdriver.find_element(By.XPATH, practice_button_xpath)
        practice_button.click()
        browser.sdriver.find_element(By.XPATH, '//button[contains(., "Practice with template repository")]').click()
        ## wait till practice exercise is created. For now i will just wait for certain amount of seconds
        time.sleep(10)

def resume_practice_in_exercise_if_button_exists():
    # basically clicks 'Practice' button. So when you click 'Clone Repo' you can also select practice exercise
    resume_practice_button_xpath = '//button[contains(., "Resume practice in exercise")]'
    if 0 != len(browser.sdriver.find_elements(By.XPATH, resume_practice_button_xpath)):
        practice_button = browser.sdriver.find_element(By.XPATH, resume_practice_button_xpath)
        # practice_button.click()
        browser.sdriver.execute_script("arguments[0].click();", practice_button)

        time.sleep(3)