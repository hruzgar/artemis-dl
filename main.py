import time
from ArtemisMainPage import ArtemisMainPage
from ArtemisCourse import ArtemisCourse
from ArtemisExercise import ArtemisExercise
import Artemis
from browser import sdriver
    
def run():
    sdriver.get('https://artemis.in.tum.de/')
    Artemis.enable_dark_mode()
    Artemis.login()
    time.sleep(2)
    # era = ArtemisExercise(course_name='Einführung in die Rechnerarchitektur (WS22/23)', exercise_name='H01 - Zahlensysteme', exercise_link='https://artemis.in.tum.de/courses/218/exercises/7838')
    # era.open()
    # era.download_exercise()

    pgdp = ArtemisExercise(course_name='', exercise_name='W11B01 - Pengu Survivors', exercise_link='https://artemis.in.tum.de/courses/201/exercises/8880')
    pgdp.open()
    pgdp.download_exercise()

if __name__ == '__main__':
    run()

