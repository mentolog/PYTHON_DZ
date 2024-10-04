from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Инициализация вебдрайвера
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# Установка неявного ожидания (будет применяться ко всем элементам)
driver.implicitly_wait(30)  # Неявное ожидание до 30 секунд

try:
    # Шаг 1: Переход на страницу
    driver.get("http://uitestingplayground.com/ajax")

    # Шаг 2: Поиск синей кнопки и нажатие
    blue_button = driver.find_element(By.CSS_SELECTOR, "button#ajaxButton")
    blue_button.click()

    # Шаг 3: Явное ожидание появления зеленой плашки с текстом (не привязано ко времени)
    WebDriverWait(driver, 30).until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, "div#content > p.bg-success"),
                                         "Data loaded with AJAX get request.")
    )

    # Шаг 4: Получение текста и вывод в консоль
    green_text = driver.find_element(By.CSS_SELECTOR, "div#content > p.bg-success").text
    print(green_text)  # Ожидаемый вывод: "Data loaded with AJAX get request."

finally:
    # Закрытие браузера
    driver.quit()
