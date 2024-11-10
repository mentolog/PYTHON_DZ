import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

@allure.step("Настройка браузера и переход на страницу калькулятора")
def setup_browser():
    """
    Настраивает браузер для теста и открывает страницу калькулятора.

    :return: WebDriver instance
    :rtype: selenium.webdriver.Chrome
    """
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.implicitly_wait(10)
    with allure.step("Переход на URL калькулятора"):
        driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    return driver
