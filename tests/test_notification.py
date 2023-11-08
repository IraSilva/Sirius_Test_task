import time
import pytest

from pages.notification_page import NotificationPage
from data.credentials import credentials


class TestNotificationPage:
    """Тестирование страницы уведомления об успешной регистрации"""

    @pytest.mark.smoke_test
    def test_02_01_check_success_message(self, driver, registration_page):
        """Проверка правильности сообщения об отправке письма при успешной регистрации"""

        registration_page.get_surname_field().send_keys(credentials["surname"])
        registration_page.get_name_field().send_keys(credentials["username"])
        registration_page.get_patronymic_field().send_keys(credentials["patronymic"])
        registration_page.get_date_field().send_keys(credentials["date_birth"])
        time.sleep(3)
        registration_page.get_email_field().send_keys(credentials["email"])
        registration_page.get_vosh_login_field().send_keys(credentials["vosh_login"])
        registration_page.get_phone_field().send_keys(credentials["phone"])
        registration_page.get_snils_field().send_keys(credentials["snils"])
        registration_page.get_profession_field().send_keys(credentials["profession"])
        registration_page.get_country_field().click()
        registration_page.get_choose_country().click()
        registration_page.get_city_field().send_keys(credentials["city"])
        registration_page.get_organisation_field().send_keys(credentials["organization"])
        registration_page.get_school_field().send_keys(credentials["school"])
        registration_page.get_class_field().send_keys(credentials["class"])
        registration_page.get_checkbox_confirmation_of_veracity().click()
        registration_page.get_checkbox_users_agreement_and_personal_data().click()
        registration_page.get_checkbox_familiarized_with_the_rules().click()
        registration_page.get_confirmation_button().click()

        notification_page = NotificationPage(driver)
        success_message = notification_page.get_success_message().text
        assert "Мы отправили письмо с персональной ссылкой для выполнения заданий на почту" in success_message, \
               f"Сообщение неверное"

    @pytest.mark.smoke_test
    def test_02_02_check_email_in_success_message(self, driver, registration_page):
        """Проверка правильности электронной почты в сообщении об успешной регистрации"""

        registration_page.get_surname_field().send_keys(credentials["surname"])
        registration_page.get_name_field().send_keys(credentials["username"])
        registration_page.get_patronymic_field().send_keys(credentials["patronymic"])
        registration_page.get_date_field().send_keys(credentials["date_birth"])
        time.sleep(3)
        registration_page.get_email_field().send_keys(credentials["email"])
        registration_page.get_vosh_login_field().send_keys(credentials["vosh_login"])
        registration_page.get_phone_field().send_keys(credentials["phone"])
        registration_page.get_snils_field().send_keys(credentials["snils"])
        registration_page.get_profession_field().send_keys(credentials["profession"])
        registration_page.get_country_field().click()
        registration_page.get_choose_country().click()
        registration_page.get_city_field().send_keys(credentials["city"])
        registration_page.get_organisation_field().send_keys(credentials["organization"])
        registration_page.get_school_field().send_keys(credentials["school"])
        registration_page.get_class_field().send_keys(credentials["class"])
        registration_page.get_checkbox_confirmation_of_veracity().click()
        registration_page.get_checkbox_users_agreement_and_personal_data().click()
        registration_page.get_checkbox_familiarized_with_the_rules().click()
        registration_page.get_confirmation_button().click()

        notification_page = NotificationPage(driver)
        success_msg = notification_page.get_success_message().text
        email_address = credentials["email"]
        assert email_address in success_msg, f"В сообщении указана неверная почта"

    def test_02_03_check_back_button(self, driver, registration_page):
        """Проверка присутствия и кликабельности кнопки Назад на странице успешной регистрации"""

        registration_page.get_surname_field().send_keys(credentials["surname"])
        registration_page.get_name_field().send_keys(credentials["username"])
        registration_page.get_patronymic_field().send_keys(credentials["patronymic"])
        registration_page.get_date_field().send_keys(credentials["date_birth"])
        time.sleep(3)
        registration_page.get_email_field().send_keys(credentials["email"])
        # time.sleep(5)
        registration_page.get_vosh_login_field().send_keys(credentials["vosh_login"])
        registration_page.get_phone_field().send_keys(credentials["phone"])
        registration_page.get_snils_field().send_keys(credentials["snils"])
        registration_page.get_profession_field().send_keys(credentials["profession"])
        registration_page.get_country_field().click()
        registration_page.get_choose_country().click()
        registration_page.get_city_field().send_keys(credentials["city"])
        registration_page.get_organisation_field().send_keys(credentials["organization"])
        registration_page.get_school_field().send_keys(credentials["school"])
        registration_page.get_class_field().send_keys(credentials["class"])
        registration_page.get_checkbox_confirmation_of_veracity().click()
        registration_page.get_checkbox_users_agreement_and_personal_data().click()
        registration_page.get_checkbox_familiarized_with_the_rules().click()
        registration_page.get_confirmation_button().click()

        notification_page = NotificationPage(driver)
        assert notification_page.get_back_button().is_enabled() is True, f"Кнопка Назад отсутствует или неактивна"
