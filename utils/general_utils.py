import unicodedata
import re
import utils.browser as browser
from selenium.webdriver.common.by import By
from urllib.parse import urlparse

def slugify(value, allow_unicode=False):
    """
    Convert to ASCII if 'allow_unicode' is False. Convert spaces or repeated
    dashes to single dashes. Remove characters that aren't alphanumerics,
    underscores, or hyphens. Convert to lowercase. Also strip leading and
    trailing whitespace, dashes, and underscores.
    """
    value = str(value)
    if allow_unicode:
        value = unicodedata.normalize("NFKC", value)
    else:
        value = (
            unicodedata.normalize("NFKD", value)
            .encode("ascii", "ignore")
            .decode("ascii")
        )
    value = re.sub(r"[^\w\s-]", "", value)
    return re.sub(r"[-\s]+", "-", value).strip("-_")


def is_tum_ID(my_str):
    if len(my_str) != 7: return False
    first_part = my_str[:2]
    second_part = my_str[2:4]
    third_part = my_str[4:]
    if first_part.islower() is False or first_part.isalpha() is False: return False
    if second_part.isnumeric() is False or second_part.isnumeric() is False: return False
    if third_part.islower() is False or third_part.isalpha() is False: return False
    return True

def is_valid_artemis_course_link(my_str):
    pattern = re.compile(r'^https://artemis(?:\.(?:in|cit))?\.tum\.de/courses/\d+(?:/exercises)?$')
    if pattern.match(my_str): return True
    return False


def get_exercise_tags_on_page():
    exercise_tags = []

    exercise_header = browser.sdriver.find_element(By.CSS_SELECTOR, '#exercise-header')
    header_text = exercise_header.text.lower()
    if 'bonus' in header_text:
        exercise_tags.append('bonus')
    if 'homework' in header_text:
        exercise_tags.append('homework')
    if 'optional' in header_text:
        exercise_tags.append('optional')
    if 'tutorial' in header_text:
        exercise_tags.append('tutorial')
    if 'side project' in header_text:
        exercise_tags.append('side project')
    if 'quiz' in header_text:
        exercise_tags.append('quiz')
    if 'easy' in header_text:
        exercise_tags.append('easy')
    if 'medium' in header_text:
        exercise_tags.append('medium')
    if 'hard' in header_text:
        exercise_tags.append('hard')
    return exercise_tags

def extract_base_url(url: str) -> str:
    parsed = urlparse(url)
    return f"{parsed.scheme}://{parsed.netloc}"