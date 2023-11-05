import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service


@pytest.fixture(scope='function')
def driver():
    print('\nstart browser...')
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    # chrome_options.add_argument('--headless')
    driver = webdriver.Chrome(service=Service(), options=chrome_options)
    driver.implicitly_wait(10)
    yield driver
    print('\nquit browser...')
    driver.quit()


