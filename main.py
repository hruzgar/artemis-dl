import typer
import time
from ArtemisCourse import ArtemisCourse
from ArtemisExercise import ArtemisExercise
import Artemis
from utils.browser import sdriver

app = typer.Typer()


@app.command()
def hello(name: str):
    print(f"Hello {name}")


@app.command()
def dl_exercise(link: str = typer.Option(...)):
    time.sleep(1)
    sdriver.get('https://artemis.in.tum.de/')
    Artemis.enable_dark_mode()
    Artemis.login()
    time.sleep(2)
    exercise = ArtemisExercise(exercise_link=link)
    exercise.open()
    exercise.collapse_all_parts()
    exercise.download_exercise()

@app.command()
def dl_course(link: str = typer.Option(...)):
    sdriver.get('https://artemis.in.tum.de/')
    Artemis.enable_dark_mode()
    Artemis.login()
    time.sleep(2)
    course = ArtemisCourse(course_link=link)
    course.open()
    course.download_all_exercises()


if __name__ == "__main__":
    app()