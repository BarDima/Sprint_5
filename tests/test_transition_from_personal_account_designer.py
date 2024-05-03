from locators import StellaLocator
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

class TestStellaFromPersonalToDesigner:
    def test_transition_personal_account_to_designer(self, driver):
        driver.find_element(*StellaLocator.BUTTON_ENTRANCE_TO_ACCOUNT).click()
        driver.find_element(*StellaLocator.EMAIL_FIELD).send_keys('qwer@qw.ru')
        driver.find_element(*StellaLocator.PASSWORD_FIELD).send_keys('123456')
        driver.find_element(*StellaLocator.BUTTON_ENTRANCE).click()
        driver.find_element(*StellaLocator.PERSONAL_ACCOUNT).click()
        driver.find_element(*StellaLocator.DESIGNER_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, "*//h1[text()='Соберите бургер']")))
        expected_url = 'https://stellarburgers.nomoreparties.site/'
        assert driver.current_url == expected_url
