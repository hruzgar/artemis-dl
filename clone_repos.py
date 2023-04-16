import git
import const;

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

def clone_all_repos(repo_urls, exercise_name):
    for repo in repo_urls:
        clone_git_https_repo_with_credentials(repo_urls[repo], const.download_dir.joinpath(exercise_name))


