from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Запуск браузера
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.implicitly_wait(10)

try:
    # Открыть сайт магазина
    driver.get('https://www.saucedemo.com/')

    # Авторизация
    driver.find_element(By.ID, 'user-name').send_keys('standard_user')
    driver.find_element(By.ID, 'password').send_keys('secret_sauce')
    driver.find_element(By.ID, 'login-button').click()

    # Добавление товаров в корзину
    driver.find_element(By.ID, 'add-to-cart-sauce-labs-backpack').click()
    driver.find_element(By.ID, 'add-to-cart-sauce-labs-bolt-t-shirt').click()
    driver.find_element(By.ID, 'add-to-cart-sauce-labs-onesie').click()

    # Переход в корзину
    driver.find_element(By.CLASS_NAME, 'shopping_cart_link').click()

    # Проверка количества товаров в корзине
    cart_count = driver.find_element(By.CLASS_NAME, 'shopping_cart_badge').text
    assert cart_count == '3', f"Expected 3 items in cart, but got {cart_count}"

    # Нажатие кнопки Checkout
    driver.find_element(By.ID, 'checkout').click()

    # Заполнение формы пользователя
    driver.find_element(By.ID, 'first-name').send_keys('John')
    driver.find_element(By.ID, 'last-name').send_keys('Smith')
    driver.find_element(By.ID, 'postal-code').send_keys('123456')
    driver.find_element(By.ID, 'continue').click()

    # Получение итоговой стоимости
    total_price = driver.find_element(By.CLASS_NAME, 'summary_total_label').text
    assert total_price == 'Total: $58.29', f"Expected total price to be $58.29, but got {total_price}"

    # Проверка налога
    tax = driver.find_element(By.CLASS_NAME, 'summary_tax_label').text
    assert tax == 'Tax: $4.32', f"Expected tax to be $4.32, but got {tax}"

    # Завершение заказа
    driver.find_element(By.ID, 'finish').click()

finally:
    # Закрытие браузера
    driver.quit()
