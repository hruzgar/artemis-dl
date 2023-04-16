import os
import time
import requests
import base64
from selenium.webdriver.common.print_page_options import PrintOptions
from pathlib import Path
from bs4 import BeautifulSoup
from browser import sdriver
from const import download_dir, temp_dir

def print_using_chromedriver(driver, file_name, file_path=''):
    # use can defined additional parameters if needed
    params = {'paperWidth': 8.27,
              'paperHeight': 11.69,
              'marginTop': 0.0,
              'marginBottom': 0.0,
              'marginLeft': 0.0,
              'marginRight': 0.0,
              'printBackground': True,
              'omitBackground': True,
              'landscape': False,
              'scale': 0.8}

    # call the function "execute_cdp_cmd" with the command "Page.printToPDF" with
    # parameters defined above
    data = driver.execute_cdp_cmd("Page.printToPDF", params)

    # save the output to a file.
    with open(f'{file_path}{file_name}.pdf', 'wb') as file:
        file.write(base64.b64decode(data['data']))


def print_using_selenium_method(driver, file_name, file_path=''):
    print_options = PrintOptions()
    print_options.page_height = 11.75 # orig 11.69
    print_options.page_width = 8.27 # orig 8.27
    print_options.scale = 0.3
    print_options.background = True
    print_options.margin_bottom = 0.0
    print_options.margin_top = 0.0
    print_options.margin_left = 0.0
    print_options.margin_right = 0.0
    print_options.orientation = 'portrait'
    print_options.shrink_to_fit = False
    data = driver.print_page(print_options)

    os.makedirs(file_path, exist_ok=True)
    with open(f'{file_path}\\{file_name}.pdf', 'wb') as file:
        file.write(base64.b64decode(data))
    print(f"PDF-File '{file_path}\\{file_name}.pdf' was created.")

def print_artemis_exercise_to_pdf(exercise_name, exercise_download_dir, cookie=''):
    soup = BeautifulSoup(sdriver.page_source, 'html.parser')
    soup = replace_css_file_links(soup)
    soup = remove_unnecessary_elements(soup)
    soup = remove_javascript_links(soup)
    soup = download_remote_images_and_replace_links(soup, str(temp_dir), cookie=cookie)
    os.makedirs(str(temp_dir), exist_ok=True)
    with open(str(temp_dir.joinpath('temp.html')), 'w', encoding='utf-8') as file:
        file.write(str(soup))

    original_window = sdriver.current_window_handle
    sdriver.switch_to.new_window('tab')
    sdriver.get(temp_dir.joinpath('temp.html').as_uri())
    print_using_selenium_method(sdriver, exercise_name, str(exercise_download_dir))
    sdriver.close()
    sdriver.switch_to.window(original_window)
    time.sleep(1)
    # temp_driver = chrome_wrapper.get_chromedriver()
    # temp_driver.get(temp_dir.joinpath('temp.html').as_uri())
    # print_using_selenium_method(temp_driver, exercise_name, str(exercise_download_dir))
    # temp_driver.quit()

def remove_javascript_links(soup):
    all_scripts = soup.find_all('script')
    for counter in range(len(all_scripts)):
        all_scripts[counter].decompose()
    return soup

def replace_css_file_links(soup):
    # changes the 'link' tags in the html file to direct to my custom css files (for dark mode)
    for link_tag in soup.find_all('link'):
        if (link_tag['rel'][0] != 'stylesheet'): continue
        link_tag['href'] = Path().absolute().as_uri() + '/' + link_tag['href']
    return soup    

def remove_unnecessary_elements(soup):
    ###
    # Remove Results Bar if exists
    first = soup.css.select('body > jhi-main > div > div.card > div > jhi-course-exercise-details > div > div.row > div:nth-child(1) > div:nth-child(1) > div.row.mb-2.mt-2.align-items-baseline.d-none.d-md-flex')
    if len(first) != 0: first[0].decompose()
    second = soup.css.select('body > jhi-main > div > div.card > div > jhi-course-exercise-details > div > div.row > div:nth-child(1) > div:nth-child(1) > div:nth-child(2)')
    if len(second) != 0: second[0].decompose()
    third = soup.css.select('body > jhi-main > div > div.card > div > jhi-course-exercise-details > div > div.row > div:nth-child(1) > div:nth-child(1) > div:nth-child(3)')
    if len(third) != 0: third[0].decompose()

    ###
    soup.css.select('body > jhi-main > div > div:nth-child(2) > jhi-navbar > nav')[0].decompose() # Header (ganz oben mit Artemis Zeichen und navbar)
    soup.css.select('body > jhi-main > div > div:nth-child(2) > jhi-navbar > div > div > ol')[0].decompose() # Index (Zeigt 'Courses > Prakti..')
    
    # 'Assessment:automatic'
    fourth = soup.css.select('#exercise-header > div.left-col > div.points-assessment-row.ng-star-inserted > span:nth-child(2)')
    if len(fourth) != 0: fourth[0].decompose()

    due_things = soup.css.select('#exercise-header > div.right-col > div') # Submission due: ..
    for due_thing in due_things:
        due_thing.decompose()

    soup.css.select('body > jhi-main > div > div.card > div > jhi-course-exercise-details > div > div.tab-bar.tab-bar-exercise-details.ps-3.pe-3.justify-content-end')[0].decompose() # Clone Repository part
    ###
    # remove 'Tasks' part, if exists
    fifth = soup.css.select('body > jhi-main > div > div.card > div > jhi-course-exercise-details > div > div.row > div:nth-child(1) > div > jhi-programming-exercise-instructions > div > jhi-programming-exercise-instructions-step-wizard')
    if len(fifth) != 0: fifth[0].decompose()
    ###
    # remove Community Field if exists
    list = soup.css.select('body > jhi-main > div > div.card > div > jhi-course-exercise-details > div > div.row > div.col.d-flex.flex-grow-1.justify-end')
    if len(list) != 0:
        list[0].decompose()
    ###
    soup.css.select('body > jhi-main > div > jhi-footer')[0].decompose() # Footer (About, Privacy und so ganz unten)
    return soup

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
    for img_tag in soup.find_all('img'):
        if (img_tag['src'][0] == '/'):
            image_url = 'https://artemis.in.tum.de' + img_tag['src']
        else:
            image_url = 'https://artemis.in.tum.de/' + img_tag['src']

        downloaded_image_path = download_image(image_url, local_directory, cookie)
        if downloaded_image_path:
            img_tag['src'] = downloaded_image_path

    return soup