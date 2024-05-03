from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import StellaLocator

class TestStellaRegistration:
    def test_registration(self, driver):
        driver.find_element(*StellaLocator.BUTTON_ENTRANCE_TO_ACCOUNT).click()
        driver.find_element(*StellaLocator.TEXT_REGISTER).click()
        driver.find_element(*StellaLocator.NAME_FIELD).send_keys('Ivan')
        driver.find_element(*StellaLocator.EMAIL_FIELD).send_keys('123@ya.ru')
        driver.find_element(*StellaLocator.PASSWORD_FIELD).send_keys('123456')
        driver.find_element(*StellaLocator.BUTTON_REGISTER).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, "*//a[@href='/account']")))
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/register'




