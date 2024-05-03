from selenium.webdriver.common.by import By
from locators import StellaLocator

class TestStellaIncorrectPassword:
    def test_incorrect_password(self, driver):
        driver.find_element(*StellaLocator.BUTTON_ENTRANCE_TO_ACCOUNT).click()
        driver.find_element(*StellaLocator.TEXT_REGISTER).click()
        driver.find_element(*StellaLocator.NAME_FIELD).send_keys('Ivan')
        driver.find_element(*StellaLocator.EMAIL_FIELD).send_keys('123@ya.ru')
        driver.find_element(*StellaLocator.PASSWORD_FIELD).send_keys('12345')
        driver.find_element(*StellaLocator.BUTTON_REGISTER).click()
        error_message = driver.find_element(By.XPATH, "//*[@id='root']/div/main/div/form/fieldset[3]/div/div")
        assert error_message
