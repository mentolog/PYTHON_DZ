import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CalculatorPage:
    def __init__(self, driver):
        """
        Инициализирует элементы страницы калькулятора.

        :param driver: Веб-драйвер для взаимодействия с браузером.
        :type driver: selenium.webdriver.Chrome
        """
        self.driver = driver
        self.delay_input = (By.ID, "delay")
        self.button_7 = (By.XPATH, "//span[text()='7']")
        self.button_8 = (By.XPATH, "//span[text()='8']")
        self.button_plus = (By.XPATH, "//span[text()='+']")
        self.button_equals = (By.XPATH, "//span[text()='=']")
        self.result_display = (By.ID, "result")

    @allure.step("Установить задержку: {delay_time} сек")
    def set_delay(self, delay_time: str) -> None:
        """
        Устанавливает задержку для калькулятора.

        :param delay_time: Время задержки в секундах.
        :type delay_time: str
        :return: None
        """
        with allure.step("Очистка поля ввода задержки"):
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(self.delay_input)
            ).clear()
        with allure.step("Ввод времени задержки"):
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(self.delay_input)
            ).send_keys(delay_time)

    @allure.step("Нажать кнопку '7'")
    def click_button_7(self) -> None:
        """Нажимает кнопку '7'."""
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.button_7)
        ).click()

    @allure.step("Нажать кнопку '8'")
    def click_button_8(self) -> None:
        """Нажимает кнопку '8'."""
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.button_8)
        ).click()

    @allure.step("Нажать кнопку '+'")
    def click_button_plus(self) -> None:
        """Нажимает кнопку '+'."""
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.button_plus)
        ).click()

    @allure.step("Нажать кнопку '='")
    def click_button_equals(self) -> None:
        """Нажимает кнопку '='."""
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.button_equals)
        ).click()

    @allure.step("Получить результат вычисления")
    def get_result(self) -> str:
        """
        Получает результат вычисления с экрана калькулятора.

        :return: Результат вычисления.
        :rtype: str
        """
        return WebDriverWait(self.driver, 45).until(
            EC.visibility_of_element_located(self.result_display)
        ).text
