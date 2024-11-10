from helpers import Url
from locators import Locators
from conftest import driver


class TestConstructorsSections:
# переход в раздел "Соусы"
    def test_click_to_sauces_section(self, driver):
        driver.get(Url.main_page)

        driver.find_element(*Locators.sauces_section).click()
        assert driver.find_element(*Locators.check_section).text == 'Соусы'

# переход в раздел "Булки"
    def test_click_to_buns_section(self, driver):
        driver.get(Url.main_page)

        driver.find_element(*Locators.sauces_section).click()
        driver.find_element(*Locators.buns_section).click()
        assert driver.find_element(*Locators.check_section).text == 'Булки'

# переход в раздел "Начинки"
    def test_click_to_toppings_section(self, driver):
        driver.get(Url.main_page)

        driver.find_element(*Locators.toppings_section).click()
        assert driver.find_element(*Locators.check_section).text == 'Начинки'