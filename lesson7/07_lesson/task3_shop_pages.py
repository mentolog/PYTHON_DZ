from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_input = (By.ID, "user-name")
        self.password_input = (By.ID, "password")
        self.login_button = (By.ID, "login-button")

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

class InventoryPage:
    def __init__(self, driver):
        self.driver = driver
        self.backpack_add_to_cart = (By.ID, "add-to-cart-sauce-labs-backpack")
        self.bolt_tshirt_add_to_cart = (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
        self.onesie_add_to_cart = (By.ID, "add-to-cart-sauce-labs-onesie")
        self.cart_icon = (By.CLASS_NAME, "shopping_cart_link")

    def add_backpack_to_cart(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.backpack_add_to_cart)
        ).click()

    def add_bolt_tshirt_to_cart(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.bolt_tshirt_add_to_cart)
        ).click()

    def add_onesie_to_cart(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.onesie_add_to_cart)
        ).click()

    def go_to_cart(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.cart_icon)
        ).click()

class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.checkout_button = (By.ID, "checkout")

    def click_checkout(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.checkout_button)
        ).click()

class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.first_name_input = (By.ID, "first-name")
        self.last_name_input = (By.ID, "last-name")
        self.zip_code_input = (By.ID, "postal-code")
        self.continue_button = (By.ID, "continue")

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

class SummaryPage:
    def __init__(self, driver):
        self.driver = driver
        self.total_price = (By.CLASS_NAME, "summary_total_label")
        self.tax_price = (By.CLASS_NAME, "summary_tax_label")
        self.finish_button = (By.ID, "finish")

    def get_total_price(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.total_price)
        ).text

    def get_tax_price(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.tax_price)
        ).text

    def click_finish(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.finish_button)
        ).click()
