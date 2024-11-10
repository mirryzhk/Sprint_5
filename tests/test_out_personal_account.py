from data import Login
from helpers import Url
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators
from conftest import driver

class TestPersonalArea:
# переход по клику на кнопку "Конструктор"
    def test_click_by_button_constructor(self, driver):
        driver.get(Url.main_page)

        driver.find_element(*Locators.button_personal_account).click()
        driver.find_element(*Locators.input_email_authorization).send_keys(Login.email)
        driver.find_element(*Locators.input_password_authorization).send_keys(Login.password)
        driver.find_element(*Locators.button_login).click()
        WebDriverWait(driver, 7).until(EC.visibility_of_element_located(Locators.button_set_order))
        driver.find_element(*Locators.button_personal_account).click()
        driver.find_element(*Locators.button_constructor).click()

        WebDriverWait(driver, 7).until(EC.visibility_of_element_located(Locators.button_set_order))
        assert driver.find_element(*Locators.button_set_order).is_displayed()


# переход по клику на логотип "Stellar Burger"
    def test_click_by_logo_stellar_burger(self, driver):
        driver.get(Url.main_page)

        driver.find_element(*Locators.button_personal_account).click()
        driver.find_element(*Locators.input_email_authorization).send_keys(Login.email)
        driver.find_element(*Locators.input_password_authorization).send_keys(Login.password)
        driver.find_element(*Locators.button_login).click()
        WebDriverWait(driver, 7).until(EC.visibility_of_element_located(Locators.button_set_order))
        driver.find_element(*Locators.button_personal_account).click()
        driver.find_element(*Locators.button_logo_sb).click()

        WebDriverWait(driver, 7).until(EC.visibility_of_element_located(Locators.button_set_order))
        assert driver.find_element(*Locators.button_set_order).is_displayed()