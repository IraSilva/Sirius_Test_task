from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class NotificationPage(BasePage):
    # в __init__ храним названия локаторов и их значение для данной страницы
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

        self._success_message = (By.CSS_SELECTOR, ".smt-auth-registration-panel__success-message")
        self._back_button = (By.CSS_SELECTOR, ".ui-button-icon-start.smt-auth-registration-panel__back span")
        # ...

    def get_success_message(self):
        """Метод проверяет видимость сообщения об успехе"""
        return self.element_is_visible(self._success_message)

    def get_back_button(self):
        """Метод проверяет присутствие кнопки Назад"""
        return self.element_is_present(self._back_button)

