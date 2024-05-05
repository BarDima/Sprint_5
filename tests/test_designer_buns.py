from locators import StellaLocator
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

class TestStellaBuns:
    def test_buns_clic(self, driver):
        driver.find_element(*StellaLocator.BUTTON_ENTRANCE_TO_ACCOUNT).click()
        driver.find_element(*StellaLocator.EMAIL_FIELD).send_keys('qwer@qw.ru')
        driver.find_element(*StellaLocator.PASSWORD_FIELD).send_keys('123456')
        driver.find_element(*StellaLocator.BUTTON_ENTRANCE).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((StellaLocator.CHECKOUT_BUTTON)))
        driver.find_element(*StellaLocator.SAUCES_BUTTON).click()
        driver.find_element(*StellaLocator.BUNS_BUTTON).click()
        buns_section = driver.find_element(*StellaLocator.SECTION_BUNS)
        assert buns_section