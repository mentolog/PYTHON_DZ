import pytest
from selenium import webdriver
from task3_shop_pages import LoginPage, InventoryPage, CartPage, CheckoutPage, SummaryPage
from task3_shop_config import setup_browser

def test_shop_cart():
    driver = setup_browser()

    # Логин
    login_page = LoginPage(driver)
    login_page.login("standard_user", "secret_sauce")

    # Добавление товаров в корзину
    inventory_page = InventoryPage(driver)
    inventory_page.add_backpack_to_cart()
    inventory_page.add_bolt_tshirt_to_cart()
    inventory_page.add_onesie_to_cart()
    inventory_page.go_to_cart()

    # Оформление заказа
    cart_page = CartPage(driver)
    cart_page.click_checkout()

    checkout_page = CheckoutPage(driver)
    checkout_page.fill_checkout_form("John", "Smith", "123456")

    # Проверка итоговой суммы и налога
    summary_page = SummaryPage(driver)
    total_price = summary_page.get_total_price()
    tax_price = summary_page.get_tax_price()

    assert total_price == "Total: $58.29", f"Expected Total: $58.29 but got {total_price}"
    assert tax_price == "Tax: $4.32", f"Expected Tax: $4.32 but got {tax_price}"

    # Завершение покупки
    summary_page.click_finish()

    # Закрытие браузера
    driver.quit()
