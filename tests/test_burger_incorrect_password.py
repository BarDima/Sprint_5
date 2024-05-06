import pytest
from locators import StellaLocator
from test_data_faker import get_incorrect_password
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class TestStellaIncorrectPassword:

    @pytest.mark.parametrize('password', ['1', '12345'])
    def test_incorrect_password(self, driver, password):
        name, email = get_incorrect_password()
        driver.find_element(*StellaLocator.BUTTON_ENTRANCE_TO_ACCOUNT).click()
        driver.find_element(*StellaLocator.TEXT_REGISTER).click()
        driver.find_element(*StellaLocator.NAME_FIELD).send_keys(name)
        driver.find_element(*StellaLocator.EMAIL_FIELD).send_keys(email)
        driver.find_element(*StellaLocator.PASSWORD_FIELD).send_keys(password)
        driver.find_element(*StellaLocator.BUTTON_REGISTER).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(StellaLocator.INCORRECT_PASSWORD))
        error_message = driver.find_element(*StellaLocator.INCORRECT_PASSWORD)
        assert error_message

    def test_registration_without_password(self, driver):
        name, email = get_incorrect_password()
        driver.find_element(*StellaLocator.BUTTON_ENTRANCE_TO_ACCOUNT).click()
        driver.find_element(*StellaLocator.TEXT_REGISTER).click()
        driver.find_element(*StellaLocator.NAME_FIELD).send_keys(name)
        driver.find_element(*StellaLocator.EMAIL_FIELD).send_keys(email)
        driver.find_element(*StellaLocator.BUTTON_REGISTER).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(StellaLocator.BUTTON_REGISTER))
        assert driver.find_element(*StellaLocator.REGISTRATION_TEXT).text == 'Регистрация'


