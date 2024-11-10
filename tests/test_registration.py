from data import Login
from helpers import RandomValues, Url
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators
from conftest import driver

class TestRegistration:
# Успешная регистрация аккаунта с валидными значениями email, имени и пароля
    def test_succes_account_registration_with_valid_values(self, driver):
        driver.get(Url.register_page)

        WebDriverWait(driver, 7).until(EC.visibility_of_element_located(Locators.button_signup_registration))
        driver.find_element(*Locators.input_name_registration).send_keys(RandomValues.name)
        driver.find_element(*Locators.input_email_registration).send_keys(RandomValues.email)
        driver.find_element(*Locators.input_password_registration).send_keys(RandomValues.password)
        driver.find_element(*Locators.button_signup_registration).click()

        WebDriverWait(driver, 7).until(EC.visibility_of_element_located(Locators.button_login))
        assert driver.find_element(*Locators.button_login).is_displayed()

# Появление ошибки 'Некорректный пароль' при вводе невалидного пароля
    def test_invalid_notification_with_incorrect_password(self, driver):
        driver.get(Url.register_page)

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.button_signup_registration))
        driver.find_element(*Locators.input_name_registration).send_keys(RandomValues.name)
        driver.find_element(*Locators.input_email_registration).send_keys(RandomValues.email)
        driver.find_element(*Locators.input_password_registration).send_keys(Login.invalid_password)
        driver.find_element(*Locators.button_signup_registration).click()

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.massage_error_password))
        assert driver.find_element(*Locators.massage_error_password).text == 'Некорректный пароль'