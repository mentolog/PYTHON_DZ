from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
import time

# Установка драйвера Firefox
driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

try:
    # Открыть страницу
    driver.get("http://the-internet.herokuapp.com/inputs")

    # Найти поле ввода по его xpath
    input_field = driver.find_element(By.XPATH, "//input[@type='number']")

    # Ввести текст "1000"
    input_field.send_keys("1000")

    # Очистить поле
    input_field.clear()

    # Ввести текст "999"
    input_field.send_keys("999")

    # Дождаться немного, чтобы увидеть результат (опционально)
    time.sleep(2)

finally:
    # Закрыть браузер
    driver.quit()
