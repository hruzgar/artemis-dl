import typer
import time
from ArtemisCourse import ArtemisCourse
from ArtemisExercise import ArtemisExercise
import Artemis
from utils.browser import sdriver
from config import setup

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
    username: str = typer.Option(...), 
    password: str = typer.Option(...), 
    link: str = typer.Option(...)
):
    setup(username=username, password=password, download_dir=download_path)
    sdriver.get('https://artemis.in.tum.de/')
    Artemis.enable_dark_mode()
    Artemis.login()
    time.sleep(2)
    course = ArtemisCourse(course_link=link)
    course.open()
    course.download_all_exercises()


if __name__ == "__main__":
    app()