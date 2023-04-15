import time
from ArtemisMainPage import ArtemisMainPage
from ArtemisCourse import ArtemisCourse
from browser import sdriver
    
def run():
    mainPage = ArtemisMainPage()
    ArtemisMainPage.login()
    time.sleep(2)
    pgdp = ArtemisCourse('Praktikum: Grundlagen der Programmierung WS22/23', 'https://artemis.in.tum.de/courses/201/exercises')
    pgdp.open()
    pgdp.download_one_exercise()

if __name__ == '__main__':
    run()

