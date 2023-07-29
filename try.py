import time
from ArtemisCourse import ArtemisCourse
from ArtemisExercise import ArtemisExercise
import Artemis
from config import setup
from utils.browser import sdriver
    
def run():
    # setup("","","") // add login data here
    sdriver.get('https://artemis.in.tum.de/')
    Artemis.enable_dark_mode()
    Artemis.login()
    time.sleep(2)
    ## Memory Consumption ~200mB for Google Chrome and Python
    # era = ArtemisExercise(course_name='Einführung in die Rechnerarchitektur (WS22/23)', exercise_name='H01 - Zahlensysteme', exercise_link='https://artemis.in.tum.de/courses/218/exercises/7838')
    # era.open()
    # era.download_exercise()

    # pgdp = ArtemisExercise(course_name='Praktikum: Grundlagen der Programmierung WS22/23', exercise_name='W09H03 - Videoverarbeitung', exercise_link='https://artemis.in.tum.de/courses/201/exercises/8761')
    pgdp = ArtemisExercise(exercise_link='https://artemis.in.tum.de/courses/241/exercises/9824')
    pgdp.open()
    # pgdp.collapse_all_parts()
    pgdp.download_exercise()

    # pgdp_course = ArtemisCourse('Praktikum: Grundlagen der Programmierung WS22/23', 'https://artemis.in.tum.de/courses/201/exercises')
    # pgdp_course.open()
    # pgdp_course.download_all_exercises()

    # era_course = ArtemisCourse('Einführung in die Rechnerarchitektur (WS22/23)', 'https://artemis.in.tum.de/courses/218/exercises')
    # era_course.open()
    # era_course.download_all_exercises()

if __name__ == '__main__':
    run()

