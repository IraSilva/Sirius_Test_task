from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.__wait = WebDriverWait(driver, 30, 1)

    def find_element(self, *locator):
        """Находит элемент по заданному локатору. Возвращает WebElement."""
        return self.driver.find_element(*locator)

    def go_to_element(self, element):
        """Скролит страницу к выбранному элементу, чтобы элемент стал видимым пользователю."""
        self.driver.execute_script("return arguments[0].scrollIntoView();", element)

    def element_is_present(self, *locator):
        """Ожидает проверку, что элемент присутствует в DOM-дереве, но не обязательно, что виден
        и отображается на странице. Возвращает WebElement."""
        return self.__wait.until(EC.presence_of_element_located(*locator))

    def element_is_visible(self, *locator):
        """Ожидает проверку, что элемент присутствует в DOM-дереве, виден и отображается на странице.
        Локатор - используется для поиска элемента. Возвращает WebElement."""
        self.go_to_element(self.element_is_present(*locator))
        return self.__wait.until(EC.visibility_of_element_located(*locator))

    def element_is_clickable(self, *locator):
        """Ожидает проверку, что элемент виден, отображается на странице, а также элемент активен.
        Элемент присутствует в DOM-дереве. Локатор - используется для поиска элемента."""
        return self.__wait.until(EC.element_to_be_clickable(*locator))





