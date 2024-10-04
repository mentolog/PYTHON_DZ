from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.keys import Keys

# Настройка веб-драйвера для Firefox
driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

try:
    # Открываем страницу логина
    driver.get("http://the-internet.herokuapp.com/login")

    # Находим поле для ввода имени пользователя и вводим 'tomsmith'
    username_field = driver.find_element(By.ID, "username")
    username_field.send_keys("tomsmith")

    # Находим поле для ввода пароля и вводим 'SuperSecretPassword!'
    password_field = driver.find_element(By.ID, "password")
    password_field.send_keys("SuperSecretPassword!")

    # Находим кнопку Login и нажимаем на нее
    login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
    login_button.click()

finally:
    # Закрытие браузера
    driver.quit()
