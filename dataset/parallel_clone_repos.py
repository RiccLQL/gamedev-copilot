import subprocess
from multiprocessing import Pool
from data import data_sample
import re
from typing import List

REPO_FOLDER_NAME='repos_sample'

def clone_repo(url: str):
    repo_owner_name = url.removeprefix('https://github.com/').split('/')
    owner = repo_owner_name[0]
    repo_name = repo_owner_name[1]
    subprocess.run(["git", "clone", url, f'{REPO_FOLDER_NAME}/{owner}---{repo_name}'])

def clone_repos(url_list: List[str]):
    """Finds all the github links from list data"""
    url_list = [url for url in url_list if re.match('https://github.com/', url)]

    with Pool() as pool:
        pool.map(clone_repo, url_list)


if __name__ == "__main__":
    clone_repos(data_sample)
