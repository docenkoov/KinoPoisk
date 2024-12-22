import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from UI.data.config import URL


@pytest.fixture(scope="module")
def driver():
    """Фикстура для инициализации и завершения работы веб-драйвера."""
    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()))
    driver.get(URL)
    driver.maximize_window()
    yield driver
    driver.quit()
