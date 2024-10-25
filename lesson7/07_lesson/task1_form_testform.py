import pytest
from selenium import webdriver
from task1_form_pages import FormPage
from task1_form_config import setup_browser

def test_form_submission():
    driver = setup_browser()
    form_page = FormPage(driver)
    
    # Заполнение полей формы
    form_page.set_first_name("Иван")
    form_page.set_last_name("Петров")
    form_page.set_address("Ленина, 55-3")
    form_page.set_email("test@skypro.com")
    form_page.set_phone("+7985899998787")
    form_page.set_zip_code("")  # Поле оставляем пустым
    form_page.set_city("Москва")
    form_page.set_country("Россия")
    form_page.set_job_position("QA")
    form_page.set_company("SkyPro")
    
    # Нажимаем кнопку отправки формы
    form_page.click_submit()
    
    # Ассерты можно поместить в конец
    assert "N/A" in driver.find_element_by_id("zip").get_attribute("value"), "Zip code field should be empty"
    assert driver.find_element_by_id("first-name").get_attribute("style").find("green") != -1, "First Name should be green"
    
    # Закрываем браузер
    driver.quit()
