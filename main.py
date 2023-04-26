import typer
import time
from ArtemisCourse import ArtemisCourse
from ArtemisExercise import ArtemisExercise
import Artemis
from utils.browser import sdriver
from config import setup
from utils.utils import printer, is_tum_ID, is_valid_artemis_course_link

app = typer.Typer()



@app.command()
def dl_exercise(link: str = typer.Option(...)):
    sdriver.get('https://artemis.in.tum.de/')
    Artemis.enable_dark_mode()
    Artemis.login()
    time.sleep(2)
    exercise = ArtemisExercise(exercise_link=link)
    exercise.open()
    exercise.collapse_all_parts()
    exercise.download_exercise()

@app.command()
def dl_course(
    download_path: str = typer.Option('', help="Specify Download Location"), 
    username: str = typer.Option(..., prompt=True), 
    password: str = typer.Option(..., prompt=True), 
    link: str = typer.Option(..., prompt=True, help="Course-Link from Artemis")
):
    if is_tum_ID(username) is False:
        printer('Username is not valid TUM-ID. Please try again!')
        return
    if len(password) < 8:
        printer('Password is below 8 characters. Please try again!')
        return
    if is_valid_artemis_course_link(link) is not True:
        printer('Link is not a valid Artemis-Course. Please try again!')
        return
    setup(username=username, password=password, download_dir=download_path)
    sdriver.get('https://artemis.in.tum.de/')
    Artemis.enable_dark_mode()
    if Artemis.login() == False: 
        printer('Login failed. Please check your credentials and try again!')
        return
    time.sleep(2)
    course = ArtemisCourse(course_link=link)
    course.open()
    course.download_all_exercises()


if __name__ == "__main__":
    app()