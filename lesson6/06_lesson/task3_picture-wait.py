from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

# Устанавливаем WebDriver для Chrome
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# Устанавливаем неявное ожидание
driver.implicitly_wait(10)

# 1. Переходим на сайт
driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

# 2. Ждем загрузки всех картинок (неявное ожидание установлено)
# 3. Находим третью картинку по XPath и получаем значение атрибута src
third_image = driver.find_element(By.XPATH, "(//img)[3]")
src_value = third_image.get_attribute("src")

# 4. Выводим значение атрибута src в консоль
print(f"URL третьего изображения: {src_value}")

# Закрываем браузер
driver.quit()
