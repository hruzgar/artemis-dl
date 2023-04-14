import time
import chrome_wrapper
from ArtemisMainPage import ArtemisMainPage
from selenium import webdriver
from PdfDarkMode.darkmode import convert
import printPDF
    
def run(name):
    mainPage = ArtemisMainPage()
    time.sleep(2)
    ArtemisMainPage.login("***REMOVED***", "***REMOVED***")
    time.sleep(2)
    mainPage.scrape_courses_to_class_list()
    mainPage.enterCourses(0,1)
    time.sleep(5)

if __name__ == '__main__':
    run('Started!')

