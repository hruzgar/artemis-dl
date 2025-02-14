import git
from utils import config
from utils.print import printer

def clone_git_https_repo_with_credentials(repo_url, destination_dir):
    if "bitbucket" in repo_url:
        printer("recognized old bitbucket repo URL, skipped. (all bitbucket repos were either migrated to new system or don't exist anymore)")
        return
    
    # removing username and the @ after that
    splitted_url = repo_url.split('/')
    splitted_url[2] = splitted_url[2].split('@')[1]
    repo_url = '/'.join(splitted_url)

    repo_name = repo_url.split('/')[-1].split('.')[0]
    printer(f'Cloning repo "{repo_name}"')
    repo_url_with_credentials = repo_url.replace("https://", f"https://{config.username}:{config.password}@")
    try:
        git.Repo.clone_from(repo_url_with_credentials, destination_dir.joinpath(repo_name))
    except:
        pass

def clone_all_repos(repo_urls, local_download_dir):
    for repo in repo_urls:
        clone_git_https_repo_with_credentials(repo_urls[repo], local_download_dir)


