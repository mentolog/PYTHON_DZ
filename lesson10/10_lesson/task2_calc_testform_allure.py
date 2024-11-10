import pytest
import allure
from task2_calc_pages_allure import CalculatorPage
from task2_calc_config_allure import setup_browser

@allure.title("Проверка сложения в калькуляторе")
@allure.description("Тест проверяет корректность выполнения операции сложения 7 + 8 с задержкой в 45 секунд.")
@allure.feature("Калькулятор")
@allure.severity(allure.severity_level.CRITICAL)

def test_calculator_addition():
    with allure.step("Инициализация веб-драйвера"):
        driver = setup_browser()
        
    with allure.step("Создание экземпляра страницы калькулятора"):
        calc_page = CalculatorPage(driver)

    with allure.step("Установка задержки на выполнение операций"):
        calc_page.set_delay("45")

    with allure.step("Выполнение операции сложения 7 + 8"):
        calc_page.click_button_7()
        calc_page.click_button_plus()
        calc_page.click_button_8()
        calc_page.click_button_equals()

    with allure.step("Получение и проверка результата"):
        result = calc_page.get_result()
        assert result == "15", f"Expected result to be 15, but got {result}"

    with allure.step("Закрытие веб-драйвера"):
        driver.quit()
