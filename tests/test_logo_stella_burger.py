from locators import StellaLocator
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestLogoStellaBurger:
    def test_logo(self, driver):
        driver.find_element(*StellaLocator.BUTTON_ENTRANCE_TO_ACCOUNT).click()
        driver.find_element(*StellaLocator.EMAIL_FIELD).send_keys('qwer@qw.ru')
        driver.find_element(*StellaLocator.PASSWORD_FIELD).send_keys('123456')
        driver.find_element(*StellaLocator.BUTTON_ENTRANCE).click()
        driver.find_element(*StellaLocator.PERSONAL_ACCOUNT).click()
        driver.find_element(*StellaLocator.STELLA_BURGER_LOGO).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((StellaLocator.MAKE_BURGER)))
        expected_url = 'https://stellarburgers.nomoreparties.site/'
        assert driver.current_url == expected_url
