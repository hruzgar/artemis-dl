**All the new changes to Artemis in the last year or so made the downloader unusable atm but I'm working on a complete rewrite to adjust the codebase to the new Artemis version.**

![](https://github.com/hruzgar/artemis-dl/blob/main/showcase.png)
# Introduction
**Hello and welcome to my GitHub repository!** As a student at TUM utilizing the Tum Artemis platform, I felt the need to create a way to permanently archive all of our exercises. I believe in the value of preserving knowledge, so I designed this tool to ensure I, and others, can download and access these exercises indefinitely - even 30 years down the road. This tool creates a *completely local copy* of exercises and doesn't depend on any third party services or servers to ensure the longevity.

Features:
- **Dark-Mode PDFs:** Download exercises as pdf while preserving the dark theme.
- **Exercise Repositories:** Find and download repositories (even hidden ones) of exercises directly from the Artemis git server (bitbucket).
- **One-command Course Download:** And all of this with only *one command!!*. Download full Artemis-Courses with a single command, creating a lasting local archive.

Each exercise gets the following folder structure after download (was added in the newest release 0.2.0):
```
Exercise-Name/
├── repos/
│   ├── repo/
│   ├── repo-practice/
│   └── repo-solution/
├── webpage/
│   ├── assets/
│   └── index.html
└── exercise.pdf
```

Further down, you'll encounter step-by-step installation instructions and additional details to assist in your setup. Here's to preserving our academic endeavors for the future!


# Install & Use
Currently, there are *three supported methods* to utilize this scraper. Choose the one that best fits your needs. For those less tech-savvy, the **first option is recommended** and is tailored specifically for Windows users.

<details><summary><b>1. Use preconfigured binary (Windows)(recommended)</b></summary>

#### Prerequisites
- Microsoft Edge (should be preinstalled on your PC)
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
4. If you got to here and liked the downloader, don't forget to give the repo a star ⭐. Enjoy 🥳😝
</details>
<details>
<summary><b>2. Run from source code (Windows)</b></summary>

#### Prerequisites
- Microsoft Edge (should be preinstalled on your PC)
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
<details><summary><b>3. Run from source code (Linux)</b></summary>

   
**This guide was for the older artemis-dl versions. You might be better off, using the Windows binary if you're able to. The current codebase needs some changes to choose chrome instead of MS Edge if on Linux and also someone needs to test if it works. Currently i don't have the time to do it but please make a pull request if you do..**
   
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

# Other stuff

<details><summary><b>FAQ</b></summary>
<br>
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
</details>

<details><summary><b>Roadmap</b></summary>
<br>

- Download Quizzes
   - Currently quizzes are directly skipped if found.
</details>


<details><summary><b>Behind the scenes</b></summary>
<br>

In the recent releases its not the same steps anymore. Will update this later
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

<details><summary><b>Building the Windows Binary</b></summary>
<br>

- using 'auto-py-to-exe'
- select your artemis build folder (same as repo but without ".git" folder)
- select 'One File'
- In 'Advanced > --paths' add the'site-packages' directory of your envoirenment. This will contain all the modules. For example "D:/code/artemis-dl/lib/python3.10/site-packages" for venv or "C:\\Users\\haso\\miniconda3\\envs\\scrape\\Lib\\site-packages" for conda
- In 'Additional Files' click 'Add Folder' and open root path of project. In the right input box just put a dot '.'
</details>


**Disclaimer:**
This application is provided for educational and personal use only. Users must ensure compliance with the policies of their respective educational institution and applicable laws. This software is independently developed, not affiliated with, endorsed by, or supported by any university or institution. Users assume all responsibility and risk associated with the use of this tool.
