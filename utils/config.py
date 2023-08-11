from pathlib import Path
username = ''
password = '' 
download_dir = Path().absolute().joinpath('./downloads')
temp_dir = Path().absolute().joinpath('./temp')


def setup(username, password, download_dir):
    import utils.config as config
    config.username = username
    config.password = password
    if download_dir != '':
        config.download_dir = Path(download_dir)