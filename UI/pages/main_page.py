from selenium.webdriver.common.by import By
from UI.pages.base_page import BasePage
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement
from UI.data.config import URL


class MainPage(BasePage):
    # Локаторы
    SEARCH_INPUT = (By.CSS_SELECTOR, "input[name='kp_query']")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "button[aria-label='Найти']")
    SEARCH_RESULTS = (By.CSS_SELECTOR, "div.search_results")
    NO_RESULTS_MESSAGE_SELECTOR = (By.CSS_SELECTOR, "h2.textorangebig")
    MODAL_OVERLAY = (By.CSS_SELECTOR, ".ReactModal__Overlay")
    BLOCK_LEFT_PAD = (By.CSS_SELECTOR, "#block_left_pad")

    def open(self) -> None:
        """
        Открывает главную страницу.

        :return: None
        """
        self.driver.get(URL)

    def enter_search_term(self, term: str) -> None:
        """
        Вводит текст в поле поиска.

        :param term: Текст для ввода в поле поиска.
        :return: None
        """
        search_input = self.wait_for_element(*self.SEARCH_INPUT)
        search_input.clear()
        search_input.send_keys(term)

    def close_modal_if_present(self) -> None:
        """
        Закрывает модальное окно, если оно присутствует.

        :return: None
        """
        try:
            modal_overlay = self.wait_for_element(*self.MODAL_OVERLAY)
            if modal_overlay.is_displayed():
                close_button = modal_overlay.find_element(
                    By.CSS_SELECTOR, "button.close")
                close_button.click()
        except TimeoutException:
            pass

    def click_search_button(self) -> None:
        """
        Нажимает кнопку поиска.

        :return: None
        """
        self.close_modal_if_present()
        button = self.wait_for_element_to_be_clickable(*self.SEARCH_BUTTON)
        self.driver.execute_script("arguments[0].click();", button)

    def get_search_results(self) -> str:
        """
        Возвращает текст результатов поиска или сообщение о том, что ничего
        не найдено.
        :return: str - текст результатов поиска или сообщение о том, что
        ничего не найдено.
        """
        try:
            results_element = self.wait_for_element(*self.SEARCH_RESULTS)
            if results_element.is_displayed():
                return results_element.text
            else:
                return self.get_no_results_message()
        except TimeoutException:
            raise Exception("Не удалось найти результаты поиска.")

    def get_no_results_message(self) -> str:
        """
        Возвращает текст сообщения о том, что ничего не найдено.
        :return: str - текст сообщения о том, что ничего не найдено, или None.
        """
        try:
            return WebDriverWait(self.driver, 30).until(
                EC.visibility_of_element_located(
                    self.NO_RESULTS_MESSAGE_SELECTOR)
            ).text
        except TimeoutException:
            return None

    def get_block_left_pad(self) -> WebElement:
        """
        Возвращает элемент с классом block_left_pad.
        :return: WebElement - элемент с классом block_left_pad.
        """
        return self.wait_for_element(*self.BLOCK_LEFT_PAD)
