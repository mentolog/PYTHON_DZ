import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

@allure.step("Настройка браузера и открытие страницы")
def setup_browser() -> webdriver.Chrome:
    """
    Настраивает и возвращает объект веб-драйвера для браузера Chrome.

    :return: Объект Chrome WebDriver с открытой страницей.
    """
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.implicitly_wait(10)  # Неявное ожидание
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
    return driver
