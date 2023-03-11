# This is a sample Python script.
import time
import base64
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfpage import PDFParser
from pdfminer.pdfpage import PDFDocument
import chrome_wrapper
from ArtemisMainPage import ArtemisMainPage
from selenium import webdriver


# Press Umschalt+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
def printTest(driver):
    # use can defined additional parameters if needed
    params = {'paperWidth': 8.27,
              'paperHeight': 11.69,
              'marginTop': 0.0,
              'marginBottom': 0.0,
              'marginLeft': 0.0,
              'marginRight': 0.0,
                'printBackground': True,
              'omitBackground': True,
                'landscape': False}

    # call the function "execute_cdp_cmd" with the command "Page.printToPDF" with
    # parameters defined above
    data = driver.execute_cdp_cmd("Page.printToPDF", params)

    # save the output to a file.
    with open('file_name.pdf', 'wb') as file:
        file.write(base64.b64decode(data['data']))


    # verify the page size of the PDF file created
    parser = PDFParser(open('file_name.pdf', 'rb'))
    doc = PDFDocument(parser)
    pageSizesList = []
    for page in PDFPage.create_pages(doc):
        print(page.mediabox)
        # output



def basla(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Strg+F8 to toggle the breakpoint.
    driver = chrome_wrapper.get_chrome_driver("")
    print("chrome driver alindi")
    time.sleep(2)
    mainPage = ArtemisMainPage(driver)
    mainPage.login("***REMOVED***", "***REMOVED***")
    mainPage.scrapeCoursesToList()
    mainPage.getCourseNames()
    time.sleep(3)
    printTest(driver)
    time.sleep(19)



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    basla('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
