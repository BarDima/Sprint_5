from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import StellaLocator
from test_data_faker import get_sign_up_data

class TestStellaRegistration:
    def test_registration(self, driver):
        name, email, password = get_sign_up_data()
        driver.find_element(*StellaLocator.BUTTON_ENTRANCE_TO_ACCOUNT).click()
        driver.find_element(*StellaLocator.TEXT_REGISTER).click()
        driver.find_element(*StellaLocator.NAME_FIELD).send_keys(name)
        driver.find_element(*StellaLocator.EMAIL_FIELD).send_keys(email)
        driver.find_element(*StellaLocator.PASSWORD_FIELD).send_keys(password)
        driver.find_element(*StellaLocator.BUTTON_REGISTER).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((StellaLocator.PERSONAL_ACCOUNT)))
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/register'




