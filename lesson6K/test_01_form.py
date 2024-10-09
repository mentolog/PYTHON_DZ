from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

# Открытие браузера через WebDriver
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

# Заполнение всех полей по очереди
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "first-name"))).send_keys("Иван")
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "last-name"))).send_keys("Петров")
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "address"))).send_keys("Ленина, 55-3")
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "e-mail"))).send_keys("test@skypro.com")
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "phone"))).send_keys("+7985899998787")
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "city"))).send_keys("Москва")
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "country"))).send_keys("Россия")
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "job-position"))).send_keys("QA")
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "company"))).send_keys("SkyPro")

# Ожидание и нажатие кнопки submit
submit_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "submit")))
submit_button.click()

# Проверка подсветки полей после нажатия submit
def check_field_color(field_id, expected_class):
    field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, field_id)))
    field_class = field.get_attribute("class")
    assert expected_class in field_class, f"Поле {field_id} не имеет ожидаемого класса {expected_class}"

# Поля с данными должны быть зелеными (подсветка зеленым)
green_fields = ["first-name", "last-name", "address", "e-mail", "phone", "city", "country", "job-position", "company"]
for field_id in green_fields:
    check_field_color(field_id, "is-valid")

# Поле Zip code должно быть красным (подсветка красным)
check_field_color("zip-code", "is-invalid")

# Закрытие браузера
driver.quit()
