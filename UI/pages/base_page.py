from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement


class BasePage:
    def __init__(self, driver):
        """
        Инициализация базовой страницы.
        :param driver: WebDriver для управления браузером
        (webdriver.Chrome или аналог).
        """
        self.driver = driver

    def wait_for_element(
            self, by: str, value: str, timeout: int = 30) -> WebElement:
        """
        Ожидает появления элемента на странице.
        :param by: Стратегия поиска (например, By.CSS_SELECTOR).
        :param value: Значение для поиска элемента.
        :param timeout: Время ожидания в секундах (по умолчанию 30).
        :return: Найденный элемент WebElement.
        """
        return WebDriverWait(self.driver, timeout).until(
           EC.presence_of_element_located((by, value)))

    def wait_for_element_to_be_clickable(
            self, by: str, value: str, timeout: int = 30) -> WebElement:
        """
        Ожидает, пока элемент станет кликабельным.
        :param by: Стратегия поиска (например, By.CSS_SELECTOR).
        :param value: Значение для поиска элемента.
        :param timeout: Время ожидания в секундах (по умолчанию 30).
        :return: Кликабельный элемент WebElement.
        """
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable((by, value)))

    def maximize_window(self) -> None:
        """
        Максимизирует окно браузера.
        :return: None
        """
        self.driver.maximize_window()

    def quit(self) -> None:
        """
        Закрывает браузер.
        :return: None
        """
        self.driver.quit()
