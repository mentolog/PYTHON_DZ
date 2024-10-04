from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time

# Установка и запуск драйвера
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

try:
    # Открытие страницы
    driver.get("http://the-internet.herokuapp.com/add_remove_elements/")
    
    # Нажимаем на кнопку Add Element 5 раз
    add_button = driver.find_element(By.XPATH, "//button[text()='Add Element']")
    for _ in range(5):
        add_button.click()
        time.sleep(1)  # Задержка для наглядности

    # Собираем список кнопок Delete
    delete_buttons = driver.find_elements(By.CLASS_NAME, "added-manually")
    
    # Выводим размер списка
    print(f"Количество кнопок 'Delete': {len(delete_buttons)}")

finally:
    # Закрытие браузера
    driver.quit()
