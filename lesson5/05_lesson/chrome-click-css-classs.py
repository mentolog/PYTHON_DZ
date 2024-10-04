from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time

# Инициализация WebDriver и открытие страницы
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("http://uitestingplayground.com/classattr")

# Небольшая задержка, чтобы страница загрузилась
time.sleep(2)

# Клик по синей кнопке с классом "btn-primary"
button = driver.find_element(By.XPATH, "//button[contains(@class, 'btn-primary')]")
button.click()

# Закрытие браузера
time.sleep(2)  # Небольшая задержка для визуализации результата
driver.quit()
