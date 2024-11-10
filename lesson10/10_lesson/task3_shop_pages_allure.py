import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@allure.title("Страница логина для Saucedemo")
@allure.description("Класс для выполнения действий на странице логина, включая ввод имени пользователя и пароля.")
@allure.feature("Логин и авторизация")
@allure.severity(allure.severity_level.CRITICAL)
class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_input = (By.ID, "user-name")
        self.password_input = (By.ID, "password")
        self.login_button = (By.ID, "login-button")

    @allure.step("Ввод логина и пароля и выполнение авторизации")
    def login(self, username, password):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.username_input)
        ).send_keys(username)
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.password_input)
        ).send_keys(password)
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.login_button)
        ).click()

@allure.title("Страница инвентаря для Saucedemo")
@allure.description("Класс для выполнения действий на странице инвентаря, добавления товаров в корзину и перехода в корзину.")
@allure.feature("Инвентарь")
@allure.severity(allure.severity_level.NORMAL)
class InventoryPage:
    def __init__(self, driver):
        self.driver = driver
        self.backpack_add_to_cart = (By.ID, "add-to-cart-sauce-labs-backpack")
        self.bolt_tshirt_add_to_cart = (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
        self.onesie_add_to_cart = (By.ID, "add-to-cart-sauce-labs-onesie")
        self.cart_icon = (By.CLASS_NAME, "shopping_cart_link")

    @allure.step("Добавление рюкзака в корзину")
    def add_backpack_to_cart(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.backpack_add_to_cart)
        ).click()

    @allure.step("Добавление футболки в корзину")
    def add_bolt_tshirt_to_cart(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.bolt_tshirt_add_to_cart)
        ).click()

    @allure.step("Добавление комбинезона в корзину")
    def add_onesie_to_cart(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.onesie_add_to_cart)
        ).click()

    @allure.step("Переход в корзину")
    def go_to_cart(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.cart_icon)
        ).click()

@allure.title("Страница корзины для Saucedemo")
@allure.description("Класс для выполнения действий на странице корзины, включая переход к оформлению заказа.")
@allure.feature("Корзина")
@allure.severity(allure.severity_level.NORMAL)
class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.checkout_button = (By.ID, "checkout")

    @allure.step("Нажатие на кнопку оформления заказа")
    def click_checkout(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.checkout_button)
        ).click()

@allure.title("Страница оформления заказа для Saucedemo")
@allure.description("Класс для заполнения формы оформления заказа на странице Checkout.")
@allure.feature("Оформление заказа")
@allure.severity(allure.severity_level.NORMAL)
class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.first_name_input = (By.ID, "first-name")
        self.last_name_input = (By.ID, "last-name")
        self.zip_code_input = (By.ID, "postal-code")
        self.continue_button = (By.ID, "continue")

    @allure.step("Заполнение формы оформления заказа")
    def fill_checkout_form(self, first_name, last_name, zip_code):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.first_name_input)
        ).send_keys(first_name)
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.last_name_input)
        ).send_keys(last_name)
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.zip_code_input)
        ).send_keys(zip_code)
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.continue_button)
        ).click()

@allure.title("Страница резюме для Saucedemo")
@allure.description("Класс для получения информации о цене и налогах на странице Summary, а также завершение заказа.")
@allure.feature("Резюме заказа")
@allure.severity(allure.severity_level.LOW)
class SummaryPage:
    def __init__(self, driver):
        self.driver = driver
        self.total_price = (By.CLASS_NAME, "summary_total_label")
        self.tax_price = (By.CLASS_NAME, "summary_tax_label")
        self.finish_button = (By.ID, "finish")

    @allure.step("Получение общей цены")
    def get_total_price(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.total_price)
        ).text

    @allure.step("Получение цены с налогами")
    def get_tax_price(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.tax_price)
        ).text

    @allure.step("Завершение покупки")
    def click_finish(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.finish_button)
        ).click()
