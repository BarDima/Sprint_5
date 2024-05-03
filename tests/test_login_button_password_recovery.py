from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import StellaLocator

class TestStellaLoginPasswordRecovery:
    def test_login_password_recovery(self, driver):
        driver.find_element(*StellaLocator.BUTTON_ENTRANCE_TO_ACCOUNT).click()
        driver.find_element(*StellaLocator.RESTORE_PASSWORD).click()
        driver.find_element(*StellaLocator.TEXT_LOGIN_BUTTON).click()
        driver.find_element(*StellaLocator.EMAIL_FIELD).send_keys('qwer@qw.ru')
        driver.find_element(*StellaLocator.PASSWORD_FIELD).send_keys('123456')
        driver.find_element(*StellaLocator.BUTTON_ENTRANCE).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, "*//button[text()='Оформить заказ']")))
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'
