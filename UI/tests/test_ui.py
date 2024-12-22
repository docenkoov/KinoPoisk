from UI.pages.main_page import MainPage
from UI.data.test_data import (
    SEARCH_TERM_EXISTING,
    SEARCH_TERM_NON_EXISTING,
    SEARCH_TERM_WITH_SYMBOLS,
)
import allure


@allure.step("Проверка отображения поля поиска на главной странице.")
def test_search_field_displayed(driver):
    main_page = MainPage(driver)
    main_page.open()
    assert main_page.wait_for_element(
        *main_page.SEARCH_INPUT), "Поле поиска не отображается."


@allure.step("Проверка активности кнопки поиска после ввода текста.")
def test_search_button_active(driver):
    main_page = MainPage(driver)
    main_page.open()
    main_page.enter_search_term(SEARCH_TERM_EXISTING)
    driver.execute_script("window.scrollBy(0, 400);")  # Скролл вниз
    assert main_page.wait_for_element(
        *main_page.SEARCH_BUTTON
    ).is_enabled(), "Кнопка поиска должна быть активной."


@allure.step("Проверка отображения введенных символов в поле поиска.")
def test_search_term_displayed(driver):
    main_page = MainPage(driver)
    main_page.open()
    main_page.enter_search_term(SEARCH_TERM_WITH_SYMBOLS)
    driver.execute_script("window.scrollBy(0, 400);")  # Скролл вниз
    assert main_page.wait_for_element(
        *main_page.SEARCH_INPUT
    ).get_attribute(
        "value"
    ) == SEARCH_TERM_WITH_SYMBOLS, "Введенные символы не отображаются."


@allure.step("Проверка результатов поиска существующего фильма.")
def test_search_existing_movie(driver):
    main_page = MainPage(driver)
    main_page.open()
    with allure.step(
        "Ввести название фильма в поисковую строку и нажать кнопку поиск."
    ):
        main_page.enter_search_term(SEARCH_TERM_EXISTING)
        driver.execute_script("window.scrollBy(0, 400);")  # Скролл вниз
        main_page.click_search_button()
    results_text = main_page.get_search_results()
    assert results_text, "Результаты поиска не отображаются или пусты."


@allure.step(
    "Проверка сообщения о том, что ничего не найдено "
    "при поиске несуществующего фильма."
)
def test_search_non_existing_movie(driver):
    main_page = MainPage(driver)
    main_page.open()
    with allure.step(
        "Ввести название несуществующего фильма в поисковую строку "
        "и нажать кнопку поиск."
    ):
        main_page.enter_search_term(SEARCH_TERM_NON_EXISTING)
        driver.execute_script("window.scrollBy(0, 400);")  # Скролл вниз
        main_page.click_search_button()
    no_results_message = main_page.get_no_results_message()
    expected_message = "К сожалению, по вашему запросу ничего не найдено..."
    assert no_results_message == expected_message, "Сообщение не совпадает."
