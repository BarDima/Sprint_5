from locators import StellaLocator
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestStellaSauces:
    def test_sauces_clic(self, driver):
        driver.find_element(*StellaLocator.BUTTON_ENTRANCE_TO_ACCOUNT).click()
        driver.find_element(*StellaLocator.EMAIL_FIELD).send_keys('qwer@qw.ru')
        driver.find_element(*StellaLocator.PASSWORD_FIELD).send_keys('123456')
        driver.find_element(*StellaLocator.BUTTON_ENTRANCE).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((StellaLocator.CHECKOUT_BUTTON)))
        driver.find_element(*StellaLocator.SAUCES_BUTTON).click()
        sauces_section = driver.find_element(*StellaLocator.SECTION_SAUCES)
        assert sauces_section