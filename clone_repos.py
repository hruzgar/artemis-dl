import git
import const;
from pathlib import Path

def clone_git_https_repo_with_credentials(repo_url, destination_dir):
    splitted_url = repo_url.split('/')
    splitted_url[2] = 'bitbucket.ase.in.tum.de'
    repo_url = '/'.join(splitted_url)
    repo_name = repo_url.split('/')[-1].split('.')[0]
    repo_url_with_credentials = repo_url.replace("https://", f"https://{const.student_id}:{const.password}@")
    try:
        git.Repo.clone_from(repo_url_with_credentials, destination_dir.joinpath(repo_name))
    except:
        pass

def get_repo_links_from_exercise_name(exercise_name):
    # only works with pgdp exercise names
    exercise_details = exercise_name.split(' ')[0]
    if (len(exercise_details) != 6): return 
    # exercise_details = exercise_details.lower().strip('w')
    # week_number = int(exercise_details[:2])
    # exercise_number = int(exercise_details[3:])
    # exercise_type = exercise_details[2]
    # print(f'w{str(week_number).zfill(2)}{exercise_type}{str(exercise_number).zfill(2)}')
    repo_link_first_part = f'https://bitbucket.ase.in.tum.de/scm/pgdp2223{exercise_details.lower()}/pgdp2223{exercise_details.lower()}-'
    personal_repo_link = f'{repo_link_first_part}{const.student_id}.git'
    practice_repo_link = f'{repo_link_first_part}practice-{const.student_id}.git'
    solution_repo_link = f'{repo_link_first_part}solution.git'
    tests_repo_link = f'{repo_link_first_part}tests.git'
    return {'personal':personal_repo_link,'practice':practice_repo_link,'solution':solution_repo_link,'tests':tests_repo_link}

def clone_all_repos_using_exercise_name(exercise_name):
    # only works with pgdp
    repo_urls = get_repo_links_from_exercise_name(exercise_name)
    if repo_urls == None: return
    for repo in repo_urls:
        clone_git_https_repo_with_credentials(repo_urls[repo], const.download_dir.joinpath(exercise_name))

def clone_all_repos(repo_urls, exercise_name):
    for repo in repo_urls:
        clone_git_https_repo_with_credentials(repo_urls[repo], const.download_dir.joinpath(exercise_name))


