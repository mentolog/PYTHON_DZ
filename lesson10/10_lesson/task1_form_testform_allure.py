import pytest
import allure
from selenium import webdriver
from task1_form_pages_allure import FormPage
from task1_form_config_allure import setup_browser

@allure.title("Тест отправки формы с проверкой валидности полей")
@allure.description("Тест проверяет корректное заполнение и отправку формы, а также визуальную валидацию полей.")
@allure.feature("Форма ввода данных")
@allure.severity(allure.severity_level.CRITICAL)

def test_form_submission():
    with allure.step("Инициализация браузера и переход на страницу формы"):
        driver = setup_browser()
        form_page = FormPage(driver)

    with allure.step("Заполнение полей формы"):
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

    with allure.step("Нажатие кнопки отправки формы"):
        form_page.click_submit()

    with allure.step("Проверка значения поля Zip code и стиля поля First Name"):
        zip_code_value = driver.find_element(By.ID, "zip").get_attribute("value")
        first_name_style = driver.find_element(By.ID, "first-name").get_attribute("style")

        allure.attach(
            body=f"Значение поля Zip code: {zip_code_value}",
            name="Проверка поля Zip code",
            attachment_type=allure.attachment_type.TEXT
        )
        allure.attach(
            body=f"Стиль поля First Name: {first_name_style}",
            name="Проверка стиля поля First Name",
            attachment_type=allure.attachment_type.TEXT
        )

        assert "N/A" in zip_code_value, "Zip code field should be empty"
        assert "green" in first_name_style, "First Name should be green"

    with allure.step("Закрытие браузера"):
        driver.quit()
