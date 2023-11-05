import pytest

from pages.registration_page import RegistrationPage
from data.data_urls import REGISTRATION_PAGE_URL


@pytest.fixture(scope="function")
def registration_page(driver):
    """Открывает страницу формы регистрации"""
    registration_page = RegistrationPage(driver)
    driver.get(REGISTRATION_PAGE_URL)
    return registration_page


class TestRegistrationForm:
    """..."""

    def test_01_check_registration_form_is_correct(self, driver, registration_page):
        """..."""
        heading = registration_page.get_page_header()
        assert heading is not None
