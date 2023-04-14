import chrome_wrapper
import printPDF
from ArtemisMainPage import ArtemisMainPage
import time

driver = chrome_wrapper.get_chromedriver()
time.sleep(2)
driver.get('https://artemis.in.tum.de/')
time.sleep(2)
printPDF.print_Artemis_page_to_pdf(driver, file_name='testAbi')