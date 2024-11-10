from data import Login
from helpers import Url
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators
from conftest import driver

class TestLoginIn:
# вход по кнопке «Войти в аккаунт» на главной
    def test_login_from_main_page(self, driver):
        driver.get(Url.main_page)

        driver.find_element(*Locators.button_login_authorization).click()
        driver.find_element(*Locators.input_email_authorization).send_keys(Login.email)
        driver.find_element(*Locators.input_password_authorization).send_keys(Login.password)
        driver.find_element(*Locators.button_login).click()

        WebDriverWait(driver, 7).until(EC.visibility_of_element_located(Locators.button_set_order))
        assert driver.find_element(*Locators.button_set_order).is_displayed()


# вход через кнопку «Личный кабинет»
    def test_login_by_button_personal_account(self, driver):
        driver.get(Url.main_page)

        driver.find_element(*Locators.button_personal_account).click()
        driver.find_element(*Locators.input_email_authorization).send_keys(Login.email)
        driver.find_element(*Locators.input_password_authorization).send_keys(Login.password)
        driver.find_element(*Locators.button_login).click()

        WebDriverWait(driver, 7).until(EC.visibility_of_element_located(Locators.button_set_order))
        assert driver.find_element(*Locators.button_set_order).is_displayed()

# вход через кнопку в форме регистрации
    def test_login_by_button_from_registration_form(self, driver):
        driver.get(Url.register_page)

        WebDriverWait(driver, 7).until(EC.visibility_of_element_located(Locators.button_login_recovery_form))
        driver.find_element(*Locators.button_login_recovery_form).click()
        driver.find_element(*Locators.input_email_authorization).send_keys(Login.email)
        driver.find_element(*Locators.input_password_authorization).send_keys(Login.password)
        driver.find_element(*Locators.button_login).click()

        WebDriverWait(driver, 7).until(EC.visibility_of_element_located(Locators.button_set_order))
        assert driver.find_element(*Locators.button_set_order).is_displayed()



# Вход через кнопку в форме восстановления пароля
    def test_login_by_button_from_password_recovery_form(self, driver):
        driver.get(Url.forgot_password)

        WebDriverWait(driver, 7).until(EC.visibility_of_element_located(Locators.button_login_recovery_form))
        driver.find_element(*Locators.button_login_recovery_form).click()
        driver.find_element(*Locators.input_email_authorization).send_keys(Login.email)
        driver.find_element(*Locators.input_password_authorization).send_keys(Login.password)
        driver.find_element(*Locators.button_login).click()

        WebDriverWait(driver, 7).until(EC.visibility_of_element_located(Locators.button_set_order))
        assert driver.find_element(*Locators.button_set_order).is_displayed()