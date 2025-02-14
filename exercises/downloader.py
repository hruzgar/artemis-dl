from bs4 import BeautifulSoup
from pathlib import Path
import os
import sys
import requests
import shutil
from exercises.soup_operations import remove_unnecessary_elements, remove_test_icons
import utils.browser as browser
from utils.print import printer

def save_page_to_html(exercise_name, exercise_download_dir, cookie=''):
    webpage_dir = exercise_download_dir.joinpath('webpage')
    assets_dir = webpage_dir.joinpath('assets')
    os.makedirs(str(assets_dir), exist_ok=True)
    copy_custom_css_files(assets_dir)

    soup = BeautifulSoup(browser.sdriver.page_source, 'html.parser')
    exercise_instructions_content = soup.select_one("#programming-exercise-instructions-content")
    new_soup = BeautifulSoup(str(exercise_instructions_content), "html.parser")
    full_soup = BeautifulSoup("""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Extracted Content</title>
        <style>
            body {
                margin-left: 4%;
                margin-right: 4%;
            }
        </style>
    </head>
    <body></body>
    </html>
    """, "html.parser")

    # Inject the extracted content into <body>
    full_soup.body.append(new_soup)
    full_soup.title.string = exercise_name


    # remove_base_tag(soup)
    inject_custom_css_files(full_soup, assets_dir)
    # soup = replace_css_file_links(soup)
    # remove_unnecessary_elements(soup)
    # remove_javascript_links(soup)
    remove_test_icons(full_soup)
    download_remote_images_and_replace_links(full_soup, str(assets_dir), cookie=cookie)

    with open(str(webpage_dir.joinpath('index.html')), 'w', encoding='utf-8') as file:
        file.write(str(full_soup))

def copy_custom_css_files(assets_dir):
    # copies the custom css files to the exercise directory
    if getattr(sys, 'frozen', False):
        shutil.copyfile(Path(sys._MEIPASS).joinpath('custom_css').joinpath('styles.css'), assets_dir.joinpath('styles.css'))
        shutil.copyfile(Path(sys._MEIPASS).joinpath('custom_css').joinpath('theme-dark.css'), assets_dir.joinpath('theme-dark.css'))
    else:
        shutil.copyfile(Path(__file__).parent.parent.joinpath('custom_css').joinpath('styles.css'), assets_dir.joinpath('styles.css'))
        shutil.copyfile(Path(__file__).parent.parent.joinpath('custom_css').joinpath('theme-dark.css'), assets_dir.joinpath('theme-dark.css'))
    # shutil.copyfile(Path().cwd().joinpath('custom_css').joinpath('theme-dark.css'), assets_dir.joinpath('theme-dark.css'))


def remove_base_tag(soup):
    # removes the base tag, which forces absolute paths for all links
    base_tag = soup.find('base')
    if base_tag:
        base_tag.decompose()

def inject_custom_css_files(soup, assets_dir):
    styles_css_path = assets_dir.joinpath('styles.css')
    dark_mode_css_path = assets_dir.joinpath('theme-dark.css')

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
        outside_link = False
        if (img_tag['src'][0] == '/'):
            image_url = 'https://artemis.in.tum.de' + img_tag['src']
        elif (img_tag['src'][0] == 'h'):
            image_url = img_tag['src']
            outside_link = True
        else:
            image_url = 'https://artemis.in.tum.de/' + img_tag['src']

        if outside_link:
            downloaded_image_path = download_image(image_url, local_directory, '')
        else:
            downloaded_image_path = download_image(image_url, local_directory, cookie)
        if downloaded_image_path:
            img_tag['src'] = "./assets/" + os.path.basename(downloaded_image_path)
        else:
            img_tag.decompose()
            printer('Image failed to download: ' + image_url)