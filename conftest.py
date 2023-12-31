import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

from data.data_urls import REGISTRATION_PAGE_URL
from pages.registration_page import RegistrationPage


@pytest.fixture(scope='function')
def driver():
    print('\nstart browser...')
    chrome_options = Options()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--incognito')
    # chrome_options.add_argument('--headless')
    chrome_options.add_argument('--start-maximized')
    chrome_options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(service=Service(), options=chrome_options)
    driver.implicitly_wait(10)
    yield driver
    print('\nquit browser...')
    driver.quit()


@pytest.fixture(scope="function")
def registration_page(driver):
    """Открывает страницу формы регистрации"""

    registration_page = RegistrationPage(driver)
    driver.get(REGISTRATION_PAGE_URL)
    return registration_page
