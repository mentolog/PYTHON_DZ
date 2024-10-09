from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

# Настройка WebDriver
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.implicitly_wait(10)  # Устанавливаем неявное ожидание

# Переход на нужную страницу
driver.get("http://uitestingplayground.com/textinput")

# Поиск поля ввода и ввод текста "SkyPro"
input_field = driver.find_element(By.ID, "newButtonName")
input_field.send_keys("SkyPro")

# Поиск синей кнопки и клик по ней
button = driver.find_element(By.ID, "updatingButton")
button.click()

# Получение текста кнопки после изменения
updated_button_text = button.text
print(updated_button_text)  # Вывод текста кнопки в консоль

# Закрытие браузера
driver.quit()
