from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import StellaLocator

class TestStellaPersonalAccount:
    def test_login_personal_account(self, driver):
        driver.find_element(*StellaLocator.PERSONAL_ACCOUNT).click()
        driver.find_element(*StellaLocator.EMAIL_FIELD).send_keys('qwer@qw.ru')
        driver.find_element(*StellaLocator.PASSWORD_FIELD).send_keys('123456')
        driver.find_element(*StellaLocator.BUTTON_ENTRANCE).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((StellaLocator.CHECKOUT_BUTTON)))
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'
