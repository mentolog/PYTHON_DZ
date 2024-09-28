from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time

# Настройка Chrome WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Открыть страницу
driver.get("http://uitestingplayground.com/dynamicid")

# Дать время странице загрузиться
time.sleep(2)

# Найти синюю кнопку по тексту на ней и кликнуть
button = driver.find_element(By.XPATH, "//button[contains(text(),'Button with Dynamic ID')]")
button.click()

# Дать время для проверки результата клика
time.sleep(2)

# Закрыть браузер
driver.quit()
