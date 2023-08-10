from bs4 import BeautifulSoup
import os
import requests
import exercises.element_paths as element_paths
from utils.browser import ensure_driver
import utils.browser as browser
from utils.print import printer

def save_page_to_html(exercise_name, exercise_download_dir, cookie=''):
    download_dir = exercise_download_dir.joinpath('Webpage')
    os.makedirs(str(download_dir), exist_ok=True)
    soup = BeautifulSoup(browser.sdriver.page_source, 'html.parser')
    remove_base_tag(soup)
    inject_custom_css_files(soup)
    # soup = replace_css_file_links(soup)
    remove_unnecessary_elements(soup)
    remove_javascript_links(soup)
    download_remote_images_and_replace_links(soup, str(download_dir.joinpath('images')), cookie=cookie)

    with open(str(exercise_download_dir.joinpath('Webpage').joinpath('index.html')), 'w', encoding='utf-8') as file:
        file.write(str(soup))

def remove_base_tag(soup):
    # removes the base tag, which forces absolute paths for all links
    base_tag = soup.find('base')
    if base_tag:
        base_tag.decompose()

def inject_custom_css_files(soup):
    styles_css_path = 'custom_css/styles.css'
    dark_mode_css_path = 'custom_css/theme-dark.css'

    with open(styles_css_path, 'r') as file:
        styles_css = file.read()
    
    with open(dark_mode_css_path, 'r') as file:
        dark_mode_css = file.read()

    style1 = soup.new_tag('style')
    style1.string = styles_css
    soup.head.append(style1)

    style2 = soup.new_tag('style')
    style2.string = dark_mode_css
    soup.head.append(style2)

def remove_javascript_links(soup):
    all_scripts = soup.find_all('script')
    for counter in range(len(all_scripts)):
        all_scripts[counter].decompose()

def replace_css_file_links(soup):
    # changes the 'link' tags in the html file to direct to my custom css files (for dark mode)
    for link_tag in soup.find_all('link'):
        if (link_tag['rel'][0] != 'stylesheet'): continue
        # link_tag['href'] = Path().absolute().as_uri() + '/' + link_tag['href']
        if (link_tag.get('id') == 'artemis-theme-override'):
            link_tag['href'] = 'http://hruzgar.com/artemis-dl-css/theme-dark.css'
        else:
            link_tag['href'] = 'http://hruzgar.com/artemis-dl-css/styles.css'
        # link_tag['href'] = 'http://hruzgar.com/artemis-dl-css/' + link_tag['href']

def remove_css_file_links(soup):
    # removes the 'link' tags in the html file to direct to my custom css files (for dark mode)
    for link_tag in soup.find_all('link'):
        if (link_tag['rel'][0] != 'stylesheet'): continue
        link_tag.decompose()

def remove_unnecessary_elements(soup):
    ###
    # Remove Results Bar if exists
    remove_with_selector_if_exists(soup, element_paths.exercise_results_row_1)
    remove_with_selector_if_exists(soup, element_paths.exercise_results_row_2)
    remove_with_selector_if_exists(soup, element_paths.exercise_results_row_3)

    ###
    soup.css.select(element_paths.exercise_navbar)[0].decompose() # Header (ganz oben mit Artemis Zeichen und navbar)
    soup.css.select(element_paths.exercise_path_row)[0].decompose() # Index (Zeigt 'Courses > Prakti..')
    
    # 'Assessment:automatic'
    remove_with_selector_if_exists(soup, element_paths.exercise_assessment_text)

    due_things = soup.css.select(element_paths.exercise_due_date_rows) # Submission due: ..
    for due_thing in due_things:
        due_thing.decompose()

    remove_with_selector_if_exists(soup, element_paths.exercise_clone_row) # Clone Repository part
    ###
    # remove 'Tasks' part, if exists
    remove_with_selector_if_exists(soup, element_paths.exercise_tasks_row)

    ###
    # remove Community Field if exists
    remove_with_selector_if_exists(soup, element_paths.exercise_community_field)

    ###
    soup.find('jhi-footer').decompose()
    # soup.css.select(soup, element_paths.exercise_footer)[0].decompose() # Footer (About, Privacy und so ganz unten)

def remove_with_selector_if_exists(soup, css_selector):
    elements = soup.css.select(css_selector)
    if len(elements) != 0: elements[0].decompose()


def download_image(url, local_directory, cookie):
    response = requests.get(url, headers={"cookie": cookie})
    if response.status_code == 200:
        file_name = os.path.join(local_directory, url.split('/')[-1])
        with open(file_name, 'wb') as file:
            file.write(response.content)
        return file_name
    else:
        return None

def download_remote_images_and_replace_links(soup, local_directory, cookie):
    # finds all 'img' tags in html file, downloads the images and replaces the href to local image file
    os.makedirs(local_directory, exist_ok=True)
    for img_tag in soup.find_all('img'):
        if (img_tag['src'][0] == '/'):
            image_url = 'https://artemis.in.tum.de' + img_tag['src']
        else:
            image_url = 'https://artemis.in.tum.de/' + img_tag['src']

        downloaded_image_path = download_image(image_url, local_directory, cookie)
        if downloaded_image_path:
            img_tag['src'] = downloaded_image_path
        else:
            img_tag.decompose()
            printer('Image failed to download: ' + image_url)