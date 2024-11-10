import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

@allure.title("Инициализация браузера для тестов с сайтом Saucedemo")
@allure.description("Этот метод инициализирует веб-драйвер Chrome и открывает страницу Saucedemo для дальнейших тестов.")
@allure.feature("Настройка браузера для теста")
@allure.severity(allure.severity_level.CRITICAL)
def setup_browser():
    with allure.step("Настройка драйвера Chrome"):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    with allure.step("Максимизация окна браузера"):
        driver.maximize_window()

    with allure.step("Настройка неявного ожидания в 10 секунд"):
        driver.implicitly_wait(10)

    with allure.step("Открытие страницы Saucedemo"):
        driver.get("https://www.saucedemo.com/")

    return driver
