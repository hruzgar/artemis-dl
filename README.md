**Hello and welcome to my GitHub repository!** As a student at TUM utilizing the Tum Artemis platform, I felt the need to create a way to permanently archive all of your exercises. I believe in the value of preserving knowledge, so I designed this tool to ensure I, and others, can download and access these exercises indefinitely - even 30 years down the road. This tool creates a *completely local copy* of exercises and doesn't require any third party service to ensure the longevity.

Features:
- **Dark-Mode PDFs:** Download exercises preserving the dark theme.
- **Exercise Repositories:** Finds and downloads repositories (even hidden ones) of exercises directly from Tum Artemis.
- **One-command Course Download:** And all of this with only *one command!!*. Download full Artemis-Courses with a single command, creating a lasting local archive.

Further down, you'll encounter step-by-step installation instructions and additional details to assist in your setup. Here's to preserving our academic endeavors for the future!


# Install & Use
There is currently **3 supported Ways** to use this scraper. Use whichever you prefer. For non-technicals, the first solution is preferable (only works on Windows).

<details><summary><h3>1. Use preconfigured binary (Windows)(recommended)</h3></summary>

#### Prerequisites
- [Google-Chrome](https://www.google.com/chrome/)
- [Git](https://git-scm.com/download/win) (should be in PATH)
#### Installation
1. [Download binary](https://github.com/hruzgar/artemis-dl/releases/latest/download/artemis-dl_x86.exe)
2. Open "Windows Terminal" or "cmd.exe" and navigate to the folder, in which the binary exists.
```cmd
cd C:\path\to\folder
```
3. Now run 
```cmd
artemis-dl_x86.exe dl-course --username YOUR_USERNAME --password YOUR_PASSWORD --link COURSE_LINK # Showcase
artemis-dl_x86.exe dl-course --username ab12cde --password 12345678 --link "https://artemis.in.tum.de/courses/201/exercises" # Real Example
### you can also specify download location with adding '--download-path YOUR_DOWNLOAD_PATH' to the end of the command. Otherwise a folder named 'downloads' will be created in the location of the binary file. 
```
4. Enjoy 🥳😝
</details>
<details>
<summary><h3>2. Run from source code (Windows)</h3></summary>

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
3. Create a new venv envoirenment inside project folder
```cmd
python -m venv .
```
4. Activate the created envoirement
```cmd
.\Scripts\activate
```
5. Install all dependencies from requirements.txt file with
```cmd
pip install -r requirements.txt
```
6. Finally run Scraper!
```cmd
python main.py dl-course --username YOUR_USERNAME --password YOUR_PASSWORD --link COURSE_LINK # Showcase
python main.py dl-course --username ab12cde --password 12345678 --link "https://artemis.in.tum.de/courses/201/exercises" # Real Example
```

</details>
<details><summary><h3>3. Run from source code (Linux)</h3></summary>

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
python3 main.py dl-course --username YOUR_USERNAME --password YOUR_PASSWORD --link COURSE_LINK # Showcase
python3 main.py dl-course --username ab12cde --password 12345678 --link "https://artemis.in.tum.de/courses/201/exercises" # Real Example
```
</details>

<br>


# FAQ
<details><summary>Which courses are supported?</summary>

***
Currently only 2 courses are officially supported. These are:
- [Praktikum: Grundlagen der Programmierung WS22/23](https://artemis.in.tum.de/courses/201/exercises)
- [Einführung in die Rechnerarchitektur (WS22/23)](https://artemis.in.tum.de/courses/218/exercises)

Other courses might also work but weren't tested. If this scraper works for your course please send an email to [haso@ruezgar.de](mailto:haso@ruezgar.de) so i can add it to the list. If your course does not work with this scraper you could also send an email for me to support the course (i would need your login details) or just contribute to the project.
***
</details>
<details><summary>What is a course-link and how can i find it?</summary>

***
You can get the course-link of your course, if you open your Artemis Course-Page from any browser and copy the link. 
***
</details>

If you have any other questions, you can reach out to me on [haso@ruezgar.de](mailto:haso@ruezgar.de)

# Roadmap
- Generate html file for exercises
   - TODO: copy custom_css inside html file. Rename and copy to exercise folder.
   - Possible obstacles: html file might get too big.
- Download Quizzes
   - Currently quizzes are directly skipped if found.

<details><summary><h1>Behind the scenes</h1></summary>
   
1. Logs in into Artemis
2. Crawls all exercises for specified course
3. Repeatedly does Step 4-8
4. Downloads html of exercise-page
5. injects custom-css into html-page
6. prints html to pdf
7. finds all repositories on exercise-page and clones them (hidden repositories like test-repos etc are included)
8. Puts all files into a nicely named folder 🥰
9. Lets you enjoy all your exercises in the future 🤩
</details>
