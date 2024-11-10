from data import Login
from helpers import Url
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators
from conftest import driver


class TestLogOut:
# выход по кнопке «Выйти» в личном кабинете
    def test_click_logout_from_personal_account(self, driver):
        driver.get(Url.main_page)

        driver.find_element(*Locators.button_personal_account).click()
        driver.find_element(*Locators.input_email_authorization).send_keys(Login.email)
        driver.find_element(*Locators.input_password_authorization).send_keys(Login.password)
        driver.find_element(*Locators.button_login).click()
        WebDriverWait(driver, 7).until(EC.visibility_of_element_located(Locators.button_set_order))
        driver.find_element(*Locators.button_personal_account).click()
        WebDriverWait(driver, 7).until(EC.visibility_of_element_located(Locators.button_logout))
        driver.find_element(*Locators.button_logout).click()

        WebDriverWait(driver, 7).until(EC.visibility_of_element_located(Locators.button_login))
        assert driver.find_element(*Locators.button_login).is_displayed()