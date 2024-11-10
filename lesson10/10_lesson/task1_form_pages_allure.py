import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class FormPage:
    """
    Класс для работы с формой на веб-странице.
    """

    def __init__(self, driver):
        """
        Инициализирует объект FormPage с веб-драйвером и локаторами элементов формы.

        :param driver: Объект веб-драйвера Selenium.
        """
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

    @allure.step("Установка имени: {first_name}")
    def set_first_name(self, first_name: str) -> None:
        """
        Устанавливает значение в поле 'Имя'.

        :param first_name: Имя пользователя.
        """
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.first_name)
        ).send_keys(first_name)

    @allure.step("Установка фамилии: {last_name}")
    def set_last_name(self, last_name: str) -> None:
        """
        Устанавливает значение в поле 'Фамилия'.

        :param last_name: Фамилия пользователя.
        """
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.last_name)
        ).send_keys(last_name)

    @allure.step("Установка адреса: {address}")
    def set_address(self, address: str) -> None:
        """
        Устанавливает значение в поле 'Адрес'.

        :param address: Адрес пользователя.
        """
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.address)
        ).send_keys(address)

    @allure.step("Установка email: {email}")
    def set_email(self, email: str) -> None:
        """
        Устанавливает значение в поле 'Email'.

        :param email: Email пользователя.
        """
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.email)
        ).send_keys(email)

    @allure.step("Установка телефона: {phone}")
    def set_phone(self, phone: str) -> None:
        """
        Устанавливает значение в поле 'Телефон'.

        :param phone: Номер телефона пользователя.
        """
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.phone)
        ).send_keys(phone)

    @allure.step("Установка почтового индекса: {zip_code}")
    def set_zip_code(self, zip_code: str) -> None:
        """
        Устанавливает значение в поле 'Индекс'.

        :param zip_code: Почтовый индекс пользователя.
        """
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.zip_code)
        ).send_keys(zip_code)

    @allure.step("Установка города: {city}")
    def set_city(self, city: str) -> None:
        """
        Устанавливает значение в поле 'Город'.

        :param city: Город пользователя.
        """
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.city)
        ).send_keys(city)

    @allure.step("Установка страны: {country}")
    def set_country(self, country: str) -> None:
        """
        Устанавливает значение в поле 'Страна'.

        :param country: Страна пользователя.
        """
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.country)
        ).send_keys(country)

    @allure.step("Установка должности: {job_position}")
    def set_job_position(self, job_position: str) -> None:
        """
        Устанавливает значение в поле 'Должность'.

        :param job_position: Должность пользователя.
        """
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.job_position)
        ).send_keys(job_position)

    @allure.step("Установка компании: {company}")
    def set_company(self, company: str) -> None:
        """
        Устанавливает значение в поле 'Компания'.

        :param company: Название компании пользователя.
        """
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.company)
        ).send_keys(company)

    @allure.step("Нажатие кнопки 'Отправить'")
    def click_submit(self) -> None:
        """
        Кликает на кнопку 'Отправить' для отправки формы.
        """
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.submit_button)
        ).click()
