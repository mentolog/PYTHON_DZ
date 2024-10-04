from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
import time

# Установка драйвера Firefox
driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

try:
    # Открыть страницу
    driver.get("http://the-internet.herokuapp.com/entry_ad")

    # Дождаться появления модального окна
    time.sleep(2)  # Подождем немного, чтобы окно появилось

    # Найти кнопку "Close" в модальном окне и нажать на нее
    close_button = driver.find_element(By.XPATH, "//div[@class='modal-footer']/p/button")
    close_button.click()

    # Дожидаемся немного, чтобы увидеть результат
    time.sleep(2)

finally:
    # Закрыть браузер
    driver.quit()
