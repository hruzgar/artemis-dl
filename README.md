# Features
- Downloads dark-mode pdfs and repositories of exercises from [Tum Artemis](https://artemis.in.tum.de/)
  
- Can be used to download full Artemis-Courses with one command 🤯
### What does it do?
1. Logs in into Artemis
2. Crawls all exercises for specified course
3. Repeatedly does Step 4-8
4. Downloads html of exercise-page
5. injects custom-css into html-page
6. prints html to pdf
7. finds all repositories on exercise-page and clones them (hidden repositories like test-repos etc are included)
8. Puts all files into a nicely named folder 🥰
9. Lets you enjoy all your exercises in the future 🤩
# How to use
There is currently **3 supported Ways** to use this scraper. Use whichever you prefer. For non-technicals, the first solution is preferable.

## 1. Use preconfigured binary (Windows)(recommended)
#### Prerequisites
- [Google-Chrome](https://www.google.com/chrome/)
- [Git](https://git-scm.com/download/win) (should be in PATH)
#### Installation
1. Download binary artemis-dl.exe
2. Open "Windows Terminal" or "cmd.exe" and navigate to the folder, in which the binary exists.
3. Now run 
```cmd
artemis-dl.exe dl-course --link "COURSE_LINK" # Showcase
artemis-dl.exe dl-course --username YOUR_USERNAME --password YOUR_PASSWORD --link "https://artemis.in.tum.de/courses/201/exercises" # Real Example
```

## 2. Use from source code (Windows)
#### Prerequisites
- [Google-Chrome](https://www.google.com/chrome/)
- [Git](https://git-scm.com/download/win) (should be in PATH)
- [python](https://www.python.org/downloads/windows/)
- venv (should be installed together with python)
#### Installation
1. Clone Repository to your local computer with
```cmd
git clone https://github.com/hruzgar/artemis-dl.git
```
2. Now open terminal and navigate to the project-folder
```cmd
cd C:\path\to\project_folder
```
3. Create a new venv envoirenment with
```cmd
python -m venv C:\path\to\project_folder
```
4. Activate the created envoirement. Navigate to the now created 'Scripts' folder in your project and run activate
```cmd
.\Scripts\activate
```
5. Install all dependencies from requirements.txt file with
```cmd
pip install -r requirements.txt
```
6. Finally run Scraper!
```cmd
python main.py dl-course --link "COURSE_LINK" # Showcase
python main.py dl-course --link "https://artemis.in.tum.de/courses/201/exercises" # Real Example
```
## 3. Use from source code (Linux)
#### Prerequisits
- Google-Chrome
- Git
- python3
- venv for python
#### Installation
1. Clone Repo
```bash
git clone https://github.com/hruzgar/artemis-dl.git
```
2. cd into project
```bash
cd artemis-dl
```
3. Create venv envoirenment and activate afterwards
```bash
python3 -m venv .
source bin/activate
```
4. Install python modules
```bash
pip install -r requirements.txt
```
5. Run Scraper
```bash
python3 main.py dl-course --link "https://artemis.in.tum.de/courses/201/exercises"
```

# FAQ
### Which courses are supported?
Currently only 2 courses are officially supported. These are:
- [Praktikum: Grundlagen der Programmierung WS22/23](https://artemis.in.tum.de/courses/201/exercises)
- [Einführung in die Rechnerarchitektur (WS22/23)](https://artemis.in.tum.de/courses/218/exercises)

Other courses might also work but weren't tested. If this scraper works for your course please send an email to [haso@ruezgar.de](mailto:haso@ruezgar.de) so i can add it to the list. If your course does not work with this scraper you could also send an email or just contribute to the project.
### What is a course-link?
You can get the course-link of your course, if you open your Artemis Course-Page from any browser and copy the link. 

If you have any other questions, you can reach out to me on [haso@ruezgar.de](mailto:haso@ruezgar.de)
