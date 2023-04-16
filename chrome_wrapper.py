import re
import subprocess
import undetected_chromedriver as uc
from selenium import webdriver

CHROME_VERSION_REGEXP = re.compile(r'.* (\d+\.\d+\.\d+\.\d+)( .*)?')

def get_chromedriver():
    options = webdriver.ChromeOptions()
    options.headless = True
    options.add_argument('--no-sandbox')
    options.add_argument('--start-maximized')
    options.add_argument('--disable-popup-blocking')
    driver = webdriver.Chrome(options=options)
    return driver

def get_command_output(args):
    """Run a command and return the first line of stdout"""
    try:
        return subprocess.Popen(args,
                    stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                    universal_newlines=True).stdout.readline()
    except FileNotFoundError:
        return None

def get_chrome_version():
    """Determine the correct name for the chrome binary"""
    for binary_name in ['google-chrome', 'chromium', 'chrome']:
        try:
            version = get_command_output([binary_name, '--version'])
            if version is None:
                continue
            match = CHROME_VERSION_REGEXP.match(version)
            if match is None:
                continue
            return match.group(1).split('.')[0]
        except FileNotFoundError:
            pass
    return None

