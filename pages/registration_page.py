from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class RegistrationPage(BasePage):
    # в __init__ храним названия локаторов и их значение для данной страницы
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

        self._registration_page_header = (By.CSS_SELECTOR, ".login_page__title.login_page__title--normal")
        self._surname_field = (By.CSS_SELECTOR, ".test-locator-sf-lastName > label")
        self._name_field = (By.CSS_SELECTOR, ".test-locator-sf-firstName > label")
        self._patronymic_field = (By.CSS_SELECTOR, ".test-locator-sf-patronymic > label")
        self._date_field = (By.CSS_SELECTOR, ".test-locator-sf-birth-date > label")
        self._email_field = (By.CSS_SELECTOR, ".test-locator-sf-email > label")
        self._vosh_field = (By.CSS_SELECTOR, ".test-locator-sf-vosh-login-optional > label")
        self._phone_field = (By.CSS_SELECTOR, ".test-locator-sf-phone > label")
        self._snils_field = (By.CSS_SELECTOR, ".test-locator-sf-snils-opt > label")
        self._profession_field = (By.CSS_SELECTOR, ".test-locator-sf-profession > label")
        self._country_field = (By.CSS_SELECTOR, 'select.ui-schema-auth-form__country-select.ui-textinput__input-input-reset ')
        self._choose_country = (By.CSS_SELECTOR, '.ui-schema-auth-form__country-select.ui-textinput__input-input-reset option[value="RU"]')
        self._city_field = (By.CSS_SELECTOR, ".test-locator-sf-school-city > label")
        self._organization_field = (By.CSS_SELECTOR, ".test-locator-sf-school-organization > label")
        self._school_field = (By.CSS_SELECTOR, ".test-locator-sf-school-school > label")
        self._class_field = (By.CSS_SELECTOR, ".test-locator-sf-school-grade > label")
        self._first_check_box = (By.CSS_SELECTOR, ".test-locator-sf-confirmation-of-veracity label input")
        self._second_check_box = (By.CSS_SELECTOR, ".test-locator-sf-users-agreement-and-personal-data label input")
        self._third_check_box = (By.CSS_SELECTOR, ".test-locator-sf-familiarized-with-the-rules label input")
        self._confirmation_button = (By.CSS_SELECTOR, ".smt-register-form__register-btn ")
        self._error_email_message = (By.CSS_SELECTOR, ".test-locator-sf-email .ui-schema-auth-form__error")
        # ...

    def get_page_header(self):
        """Метод проверяет видимость заголовка на странице"""
        return self.element_is_visible(self._registration_page_header)

    def get_surname_field(self):
        """Метод проверяет видимость поля ввода фамилии"""
        return self.element_is_visible(self._surname_field)

    def get_name_field(self):
        """Метод проверяет видимость поля ввода имени"""
        return self.element_is_visible(self._name_field)

    def get_patronymic_field(self):
        """Метод проверяет видимость поля ввода отчества"""
        return self.element_is_visible(self._patronymic_field)

    def get_date_field(self):
        """Метод проверяет видимость поля ввода даты рождения"""
        return self.element_is_visible(self._date_field)

    def get_email_field(self):
        """Метод проверяет видимость поля ввода электронной почты"""
        return self.element_is_visible(self._email_field)

    def get_vosh_login_field(self):
        """Метод проверяет видимость поля ввода ВОШ-логина"""
        return self.element_is_visible(self._vosh_field)

    def get_phone_field(self):
        """Метод проверяет видимость поля ввода телефонного номера"""
        return self.element_is_visible(self._phone_field)

    def get_snils_field(self):
        """Метод проверяет видимость поля ввода СНИЛС"""
        return self.element_is_visible(self._snils_field)

    def get_profession_field(self):
        """Метод проверяет видимость поля ввода профессии"""
        return self.element_is_visible(self._profession_field)

    def get_country_field(self):
        """Метод проверяет видимость и кликабельность списка стран"""
        self.element_is_visible(self._country_field)
        return self.element_is_clickable(self._country_field)

    def get_choose_country(self):
        """Метод проверяет видимость и кликабельность страны в выпадающем списке"""
        self.element_is_visible(self._choose_country)
        return self.element_is_clickable(self._choose_country)

    def get_city_field(self):
        """Метод проверяет видимость поля ввода города"""
        return self.element_is_visible(self._city_field)

    def get_organisation_field(self):
        """Метод проверяет видимость поля ввода организации"""
        return self.element_is_visible(self._organization_field)

    def get_school_field(self):
        """Метод проверяет видимость поля ввода школы"""
        return self.element_is_visible(self._school_field)

    def get_class_field(self):
        """Метод проверяет видимость поля ввода класса"""
        return self.element_is_visible(self._class_field)

    def get_checkbox_confirmation_of_veracity(self):
        """Метод проверяет видимость и кликабельность первого чек-бокса"""
        self.element_is_visible(self._first_check_box)
        return self.element_is_clickable(self._first_check_box)

    def get_checkbox_users_agreement_and_personal_data(self):
        """Метод проверяет видимость и кликабельность второго чек-бокса"""
        self.element_is_visible(self._second_check_box)
        return self.element_is_clickable(self._second_check_box)

    def get_checkbox_familiarized_with_the_rules(self):
        """Метод проверяет видимость и кликабельность третьего чек-бокса"""
        self.element_is_visible(self._third_check_box)
        return self.element_is_clickable(self._third_check_box)

    def get_confirmation_button(self):
        """Метод проверяет наличие кнопки 'Перейти к тестированию'"""
        return self.element_is_present(self._confirmation_button)

    def get_error_email_message(self):
        """Метод проверяет видимость сообщения об ошибке при вводе неправильного email"""
        return self.element_is_visible(self._error_email_message)





