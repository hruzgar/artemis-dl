import time
from selenium import webdriver
from ArtemisMainPage import ArtemisMainPage
from const import student_id, password
    
def run():
    mainPage = ArtemisMainPage()
    time.sleep(2)
    ArtemisMainPage.login(student_id, password)
    time.sleep(2)
    mainPage.scrape_courses_to_class_list()
    mainPage.enterCourses(0,1)
    time.sleep(5)

if __name__ == '__main__':
    run()

