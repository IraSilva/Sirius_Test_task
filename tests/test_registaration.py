import time
import pytest
from selenium.common import TimeoutException

from data.credentials import credentials, surnames, names, patronymics, phone_numbers, invalid_emails


class TestRegistrationPage:
    """Тестирование страницы регистрации"""

    @pytest.mark.xfail(reason="Опечатка в заголовке")
    @pytest.mark.smoke_test
    def test_01_01_check_registration_form_heading_is_correct(self, driver, registration_page):
        """Проверка, правильности заголовка регистрационной формы"""
        heading = registration_page.get_page_header()
        heading_text = heading.text
        assert heading_text == "Автотесты. Основная олимпиада", f"Заголовок регистрационной формы отсутствует " \
                                                                f"или является некорректным: {heading_text}"

    @pytest.mark.smoke_test
    def test_01_02_registration_with_correct_data(self, driver, registration_page):
        """Проверка возможности регистрации, когда все поля заполнены корректными данными"""

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
        assert registration_page.get_confirmation_button().is_enabled() is True, f"Кнопка отсутствует или неактивна"

    @pytest.mark.smoke_test
    def test_01_03_registration_with_all_empty_fields(self, driver, registration_page):
        """Проверка возможности регистрации, когда все поля не заполнены"""

        registration_page.get_checkbox_confirmation_of_veracity().click()
        registration_page.get_checkbox_users_agreement_and_personal_data().click()
        registration_page.get_checkbox_familiarized_with_the_rules().click()
        time.sleep(3)
        assert registration_page.get_confirmation_button().is_enabled() is False, f"Кнопка регистрации активна при " \
                                                                                  f"незаполненных полях"

    @pytest.mark.parametrize('surname', surnames)
    def test_01_04_registration_with_different_valid_surnames(self, driver, registration_page, surname):
        """Проверка возможности регистрации с различными корректными значениями в поле Фамилия"""

        registration_page.get_surname_field().send_keys(surname)
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
        time.sleep(3)
        assert registration_page.get_confirmation_button().is_enabled() is True, f"Кнопка отсутствует или неактивна"

    @pytest.mark.parametrize('name', names)
    def test_01_05_registration_with_different_valid_names(self, driver, registration_page, name):
        """Проверка возможности регистрации с различными корректными значениями в поле Имя"""

        registration_page.get_surname_field().send_keys(credentials["surname"])
        registration_page.get_name_field().send_keys(name)
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
        time.sleep(3)
        assert registration_page.get_confirmation_button().is_enabled() is True, f"Кнопка отсутствует или неактивна"

    @pytest.mark.parametrize('patronymic', patronymics)
    def test_01_06_registration_with_different_valid_patronymics(self, driver, registration_page, patronymic):
        """Проверка возможности регистрации с различными корректными значениями в поле Отчество"""

        registration_page.get_surname_field().send_keys(credentials["surname"])
        registration_page.get_name_field().send_keys(credentials["username"])
        registration_page.get_patronymic_field().send_keys(patronymic)
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
        time.sleep(3)
        assert registration_page.get_confirmation_button().is_enabled() is True, f"Кнопка отсутствует или неактивна"

    @pytest.mark.parametrize('phone', phone_numbers)
    def test_01_07_registration_with_different_valid_phone_numbers(self, driver, registration_page, phone):
        """Проверка возможности регистрации с различными корректными форматами телефонного номера"""

        registration_page.get_surname_field().send_keys(credentials["surname"])
        registration_page.get_name_field().send_keys(credentials["username"])
        registration_page.get_patronymic_field().send_keys(credentials["patronymic"])
        registration_page.get_date_field().send_keys(credentials["date_birth"])
        time.sleep(3)
        registration_page.get_email_field().send_keys(credentials["email"])
        registration_page.get_vosh_login_field().send_keys(credentials["vosh_login"])
        registration_page.get_phone_field().send_keys(phone)
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
        time.sleep(3)
        assert registration_page.get_confirmation_button().is_enabled() is True, f"Кнопка отсутствует или неактивна"

    @pytest.mark.parametrize('invalid_email', invalid_emails)
    def test_01_08_registration_with_invalid_emails(self, driver, registration_page, invalid_email):
        """Проверка правильности сообщения об ошибке при вводе некорректного email"""

        registration_page.get_email_field().send_keys(invalid_email)
        try:
            message = registration_page.get_error_email_message()
            message_text = message.text
            assert message_text == "Неверный email", f"Сообщение о некорректном email отсутствует " \
                                                     f"или является неправильным для {invalid_email}"
        except TimeoutException:
            print(f" Сообщение о некорректном email отсутствует для {invalid_email}")

