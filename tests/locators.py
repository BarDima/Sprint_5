from selenium.webdriver.common.by import By
class StellaLocator:
    BUTTON_ENTRANCE_TO_ACCOUNT = (By.XPATH, "*//div/button[text()='Войти в аккаунт']")#кнопка войти в аккаунт
    TEXT_REGISTER = (By.XPATH, "*//a[@href='/register']")#текст зарегистрироваться
    NAME_FIELD = (By.XPATH, "//*[@id='root']/div/main/div/form/fieldset[1]/div/div/input")  # поле имя
    EMAIL_FIELD = (By.XPATH, "*//input[@name = 'name']") #поле Email
    PASSWORD_FIELD = (By.XPATH, "*//input[@name='Пароль']")#поле пароль
    BUTTON_REGISTER = (By.XPATH, "*//button[text()='Зарегистрироваться']")#кнопка зпрегистрироваться
    INVALID_PASSWORD = (By.XPATH, "//*[@id='root']/div/main/div/form/fieldset[3]/div/div")#ошибка некорректный ввод пароля
    TEXT_LOGIN_BUTTON = (By.XPATH, "*//a[@href='/login']")#текст войти
    BUTTON_ENTRANCE = (By.XPATH, "*//button[text()='Войти']")#кнопка войти
    PERSONAL_ACCOUNT = (By.XPATH, "*//p[text()='Личный Кабинет']")#личный кабинет
    RESTORE_PASSWORD = (By.XPATH, "*//a[@href='/forgot-password']")# текст восстановление пароля
    DESIGNER_BUTTON = (By.XPATH, "*//p[text()='Конструктор']")#кнопка конструктор
    STELLA_BURGER_LOGO = (By.XPATH, "*//div/a[@href='/']")#логотип Stella Burger
    LOGOUT_BUTTON = (By.XPATH, "*//button[text()='Выход']")# кнопка "Выход"
    SAUCES_BUTTON = (By.XPATH, "*//span[text()='Соусы']")#кнопка соусы
    BUNS_BUTTON = (By.XPATH, "*//span[text()='Булки']")#кнопка булки
    FILLINGS_BUTTON = (By.XPATH, "*//span[text()='Начинки']")#кнопка начинки
    SECTION_BUNS = (By.XPATH, "*//div/h2[text()='Булки']")
    SECTION_SAUCES = (By.XPATH, "*//div/h2[text()='Соусы']")
    SECTION_FILLINGS = (By.XPATH, "*//h2[text()='Начинки']")
