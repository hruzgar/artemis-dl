import chrome_wrapper
import printPDF
from ArtemisMainPage import ArtemisMainPage
import time

driver = chrome_wrapper.get_chromedriver()
mainPage = ArtemisMainPage(driver)
mainPage.login("***REMOVED***", "***REMOVED***")
time.sleep(2)
driver.get('https://artemis.in.tum.de/courses/201/exercises/8880')
time.sleep(2)
printPDF.print_Artemis_page_to_pdf(driver, file_name='testAbi')