import unicodedata
from rich import print
import re

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

def printer(message):
    print(f'[bold red]\[artemis-dl][/] {message}')

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
    pattern = re.compile(r'^https://artemis\.in\.tum\.de/courses/\d+/exercises(/(\d+))?$')
    if pattern.match(my_str): return True
    return False