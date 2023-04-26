from pathlib import Path
import config
username = ''
password = '' 
download_dir = Path().absolute().joinpath('downloads')
temp_dir = Path().absolute().joinpath('temp')


def setup(username, password, download_dir):
    config.username = username
    config.password = password
    if download_dir != '':
        config.download_dir = Path(download_dir)