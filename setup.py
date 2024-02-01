import os
import zipfile
import requests
from pathlib import Path

def download_and_extract(url, destination):
    response = requests.get(url)
    zip_file = Path(destination).with_suffix('.zip')
    
    with open(zip_file, 'wb') as f:
        f.write(response.content)

    with zipfile.ZipFile(zip_file, 'r') as zip_ref:
        zip_ref.extractall(destination)

    os.remove(zip_file)

# Set your preferred directory
download_dir = '/path/to/download'

# Download and extract Chrome
chrome_url = 'https://edgedl.me.gvt1.com/edgedl/chrome/chrome-for-testing/121.0.6167.85/linux64/chrome-linux64.zip'
chrome_destination = os.path.join(download_dir, 'chrome')
download_and_extract(chrome_url, chrome_destination)

# Download and extract ChromeDriver
chromedriver_url = 'https://edgedl.me.gvt1.com/edgedl/chrome/chrome-for-testing/121.0.6167.85/linux64/chromedriver-linux64.zip'
chromedriver_destination = os.path.join(download_dir, 'chromedriver')
download_and_extract(chromedriver_url, chromedriver_destination)

# Download and extract Chrome Headless Shell
chrome_headless_url = 'https://edgedl.me.gvt1.com/edgedl/chrome/chrome-for-testing/121.0.6167.85/linux64/chrome-headless-shell-linux64.zip'
chrome_headless_destination = os.path.join(download_dir, 'chrome-headless-shell')
download_and_extract(chrome_headless_url, chrome_headless_destination)

# Print the paths to the extracted files
print(f'Chrome: {chrome_destination}')
print(f'ChromeDriver: {chromedriver_destination}')
print(f'Chrome Headless Shell: {chrome_headless_destination}')