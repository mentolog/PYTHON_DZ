from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CalculatorPage:
    def __init__(self, driver):
        self.driver = driver
        self.delay_input = (By.ID, "delay")
        self.button_7 = (By.XPATH, "//span[text()='7']")
        self.button_8 = (By.XPATH, "//span[text()='8']")
        self.button_plus = (By.XPATH, "//span[text()='+']")
        self.button_equals = (By.XPATH, "//span[text()='=']")
        self.result_display = (By.ID, "result")

    def set_delay(self, delay_time):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.delay_input)
        ).clear()
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.delay_input)
        ).send_keys(delay_time)

    def click_button_7(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.button_7)
        ).click()

    def click_button_8(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.button_8)
        ).click()

    def click_button_plus(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.button_plus)
        ).click()

    def click_button_equals(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.button_equals)
        ).click()

    def get_result(self):
        return WebDriverWait(self.driver, 45).until(
            EC.visibility_of_element_located(self.result_display)
        ).text
