from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import chromedriver_autoinstaller

chromedriver_autoinstaller.install()

def create_driver(headless=True):
    options = Options()
    if headless:
        options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)
    return driver

def fetch_page_with_selenium(url, driver):
    driver.get(url)
    return driver.page_source
