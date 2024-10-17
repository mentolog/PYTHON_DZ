import pytest
from selenium import webdriver
from task2_calc_pages import CalculatorPage
from task2_calc_config import setup_browser

def test_calculator_addition():
    driver = setup_browser()
    calc_page = CalculatorPage(driver)
    
    # Установка задержки
    calc_page.set_delay("45")
    
    # Нажимаем на 7 + 8 =
    calc_page.click_button_7()
    calc_page.click_button_plus()
    calc_page.click_button_8()
    calc_page.click_button_equals()
    
    # Получаем результат и проверяем его
    result = calc_page.get_result()
    assert result == "15", f"Expected result to be 15, but got {result}"
    
    # Закрываем браузер
    driver.quit()
