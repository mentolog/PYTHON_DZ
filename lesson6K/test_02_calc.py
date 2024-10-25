from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

# Запускаем браузер
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()

# Переходим на страницу калькулятора
driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

try:
    # Вводим значение задержки 45 секунд
    delay_input = driver.find_element(By.ID, "delay")
    delay_input.clear()
    delay_input.send_keys("45")
    
    # Нажимаем кнопки 7 + 8 =
    driver.find_element(By.XPATH, "//span[text()='7']").click()
    driver.find_element(By.XPATH, "//span[text()='+']").click()
    driver.find_element(By.XPATH, "//span[text()='8']").click()
    driver.find_element(By.XPATH, "//span[text()='=']").click()

    # Явное ожидание появления результата (45 секунд + время выполнения)
    result_element = WebDriverWait(driver, 60).until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#result"), "15")
    )

    # Получаем результат
    result = driver.find_element(By.ID, "result").text

    # Проверяем, что результат равен 15
    assert result == "15", f"Ошибка: результат {result} не равен 15"
    print("Тест успешен, результат равен 15")

finally:
    # Закрываем браузер
    driver.quit()
