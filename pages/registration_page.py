from selenium.webdriver.common.by import By

from pages.base_page import BasePage
# from data.data_urls import


class RegistrationPage(BasePage):
    # в __init__ храним названия локаторов и их значение для данной страницы
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

        self._registration_page_header = (By.CSS_SELECTOR, ".login_page__title.login_page__title--normal")
        # ...
        # ...
        # ...

    def get_page_header(self):
        """Метод проверяет видимость заголовка страницы"""
        return self.element_is_visible(self._registration_page_header)
