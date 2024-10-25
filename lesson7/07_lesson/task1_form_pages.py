from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class FormPage:
    def __init__(self, driver):
        self.driver = driver
        self.first_name = (By.ID, "first-name")
        self.last_name = (By.ID, "last-name")
        self.address = (By.ID, "address")
        self.email = (By.ID, "email")
        self.phone = (By.ID, "phone")
        self.zip_code = (By.ID, "zip")
        self.city = (By.ID, "city")
        self.country = (By.ID, "country")
        self.job_position = (By.ID, "job")
        self.company = (By.ID, "company")
        self.submit_button = (By.CSS_SELECTOR, "button[type='submit']")

    def set_first_name(self, first_name):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.first_name)
        ).send_keys(first_name)

    def set_last_name(self, last_name):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.last_name)
        ).send_keys(last_name)

    def set_address(self, address):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.address)
        ).send_keys(address)

    def set_email(self, email):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.email)
        ).send_keys(email)

    def set_phone(self, phone):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.phone)
        ).send_keys(phone)

    def set_zip_code(self, zip_code):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.zip_code)
        ).send_keys(zip_code)

    def set_city(self, city):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.city)
        ).send_keys(city)

    def set_country(self, country):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.country)
        ).send_keys(country)

    def set_job_position(self, job_position):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.job_position)
        ).send_keys(job_position)

    def set_company(self, company):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.company)
        ).send_keys(company)

    def click_submit(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.submit_button)
        ).click()
