import os
import time
import requests
import base64
from selenium.webdriver.common.print_page_options import PrintOptions
from bs4 import BeautifulSoup
import utils.browser as browser
from utils.config import temp_dir
from utils.print import printer
from exercises.soup_operations import remove_unnecessary_elements

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
    printer(f'Creating pdf file "{file_name}.pdf"')

def print_artemis_exercise_to_pdf(exercise_name, exercise_download_dir, cookie=''):
    soup = BeautifulSoup(browser.sdriver.page_source, 'html.parser')
    soup = replace_css_file_links(soup)
    soup = remove_unnecessary_elements(soup)
    soup = remove_javascript_links(soup)
    soup = download_remote_images_and_replace_links(soup, str(temp_dir), cookie=cookie)
    os.makedirs(str(temp_dir), exist_ok=True)
    with open(str(temp_dir.joinpath('temp.html')), 'w', encoding='utf-8') as file:
        file.write(str(soup))

    original_window = browser.sdriver.current_window_handle
    browser.sdriver.switch_to.new_window('tab')
    browser.sdriver.get(temp_dir.joinpath('temp.html').as_uri())
    print_using_selenium_method(browser.sdriver, exercise_name, str(exercise_download_dir))
    browser.sdriver.close()
    browser.sdriver.switch_to.window(original_window)
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
        # link_tag['href'] = Path().absolute().as_uri() + '/' + link_tag['href']
        if (link_tag.get('id') == 'artemis-theme-override'):
            link_tag['href'] = 'http://hruzgar.com/artemis-dl-css/theme-dark.css'
        else:
            link_tag['href'] = 'http://hruzgar.com/artemis-dl-css/styles.css'
        # link_tag['href'] = 'http://hruzgar.com/artemis-dl-css/' + link_tag['href']
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
    os.makedirs(local_directory, exist_ok=True)
    for img_tag in soup.find_all('img'):
        if (img_tag['src'][0] == '/'):
            image_url = 'https://artemis.in.tum.de' + img_tag['src']
        else:
            image_url = 'https://artemis.in.tum.de/' + img_tag['src']

        downloaded_image_path = download_image(image_url, local_directory, cookie)
        if downloaded_image_path:
            img_tag['src'] = downloaded_image_path

    return soup