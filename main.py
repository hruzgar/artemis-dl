import time
import chrome_wrapper
from ArtemisMainPage import ArtemisMainPage
from selenium import webdriver
from PdfDarkMode.darkmode import convert
import printPDF

def get_page_source(driver):
    content = driver.page_source
    print(type(content))
    # print(content)
    with open('abi.html', 'w', encoding='utf-8') as file:
        file.write(content)
    pdfkit.from_file('abi.html', 'out.pdf')
    
def basla(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Strg+F8 to toggle the breakpoint.
    driver = chrome_wrapper.get_chromedriver()
    print("chrome driver alindi")
    time.sleep(2)
    mainPage = ArtemisMainPage(driver)
    time.sleep(2)
    mainPage.login("***REMOVED***", "***REMOVED***")
    time.sleep(2)
    mainPage.scrapeCoursesToClassList()
    mainPage.enterCourses(0,1)
    time.sleep(5)

def deneabi():
    driver = chrome_wrapper.get_chromedriver()
    driver.get('file:///D:/code/artemis-dl/dejj.html')
    printPDF.print_using_selenium_method(driver, 'abid.pdf')

if __name__ == '__main__':
    basla('PyCharm')
    # deneabi()

