import base64
import pdfkit
from selenium.webdriver.common.print_page_options import PrintOptions

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
    print_options.page_height = 11.69 # orig 11.69
    print_options.page_width = 8.27
    print_options.scale = 0.3
    print_options.background = True
    print_options.margin_bottom = 0.0
    print_options.margin_top = 0.0
    print_options.margin_left = 0.0
    print_options.margin_right = 0.0
    print_options.orientation = 'portrait'
    print_options.shrink_to_fit = False
    data = driver.print_page(print_options)
    print(type(data))
    print(len(data))
    with open(f'{file_path}{file_name}.pdf', 'wb') as file:
        file.write(base64.b64decode(data))