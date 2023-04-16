from selenium.webdriver.common.by import By
from browser import sdriver

def get_hidden_repo_urls():
    all_a_tags = sdriver.find_elements(By.TAG_NAME, 'a')
    all_links_in_exercise_page = []
    for a_tag in all_a_tags:
        all_links_in_exercise_page.append(a_tag.get_attribute('href'))
    repo_urls = {}
    for link in all_links_in_exercise_page:
        if link == None: continue
        if 'bitbucket' not in link: continue
        if 'solution' in link:
            if '.git' not in link: link = get_git_link_from_repo_browse_link(link)
            repo_urls['solution'] = link
        if 'tests' in link:
            if '.git' not in link: link = get_git_link_from_repo_browse_link(link)
            repo_urls['tests'] = link
    print('Hidden repos urls: ' + str(repo_urls))
    return repo_urls

def get_git_link_from_repo_browse_link(link):
    link_parts = link.split('/')
    project_name = link_parts[-4]
    repo_name = link_parts[-2]
    return f'https://bitbucket.ase.in.tum.de/scm/{project_name.lower()}/{repo_name}.git'
    


