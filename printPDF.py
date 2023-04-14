import base64
import pdfkit
from selenium.webdriver.common.print_page_options import PrintOptions
import chrome_wrapper
from pathlib import Path
import os
import requests
from bs4 import BeautifulSoup
from browser import sdriver

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
    with open(f'{file_path}{file_name}.pdf', 'wb') as file:
        file.write(base64.b64decode(data))
    print(f"PDF-File '{file_path}{file_name}.pdf' was created.")

def print_Artemis_page_to_pdf(file_name, file_path='', cookie=''):
    with open('temp/temp.html', 'w', encoding='utf-8') as file:
        file.write(sdriver.page_source)
    replace_css_file_links('temp/temp.html')
    process_html_file('temp/temp.html', 'temp/temp.html', str(Path().absolute()) + '/temp/', cookie=cookie)
    temp_driver = chrome_wrapper.get_chromedriver()
    temp_driver.get(Path().absolute().joinpath('temp/temp.html').as_uri())
    print_using_selenium_method(temp_driver, file_name, file_path)
    temp_driver.quit()


def replace_css_file_links(html_file_path):
    # changes the 'link' tags in the html file to direct to my custom css files (for dark mode)
    with open(html_file_path, 'r', encoding='utf-8') as file:
        html_content = file.read()

    soup = BeautifulSoup(html_content, 'html.parser')

    for link_tag in soup.find_all('link'):
        if (link_tag['rel'][0] != 'stylesheet'): continue
        link_tag['href'] = Path().absolute().as_uri() + '/' + link_tag['href']
        
    with open(html_file_path, 'w', encoding='utf-8') as file:
        file.write(str(soup))
    

def download_image(url, local_directory, cookie):
    response = requests.get(url, headers={"cookie": cookie})
    if response.status_code == 200:
        file_name = os.path.join(local_directory, url.split('/')[-1])
        with open(file_name, 'wb') as file:
            file.write(response.content)
        return file_name
    else:
        return None

def process_html_file(html_file_path, output_html_file_path, local_directory, cookie):
    with open(html_file_path, 'r', encoding='utf-8') as file:
        html_content = file.read()

    soup = BeautifulSoup(html_content, 'html.parser')

    # Download images and modify the HTML file
    print(soup.find_all('img'))
    for img_tag in soup.find_all('img'):
        print(img_tag)
        if (img_tag['src'][0] == '/'):
            image_url = 'https://artemis.in.tum.de' + img_tag['src']
        else:
            image_url = 'https://artemis.in.tum.de/' + img_tag['src']

        downloaded_image_path = download_image(image_url, local_directory, cookie)
        if downloaded_image_path:
            img_tag['src'] = downloaded_image_path

    # Save the modified HTML file
    with open(output_html_file_path, 'w', encoding='utf-8') as file:
        file.write(str(soup))

    print(f"Modified HTML file saved to {output_html_file_path}")


# Create the local directory if it doesn't exist
# os.makedirs(local_directory, exist_ok=True)