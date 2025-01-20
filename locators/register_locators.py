from selenium.webdriver.common.by import By


class RegisterLocators:
    REGISTRATION_NAME = (By.XPATH, '//label[ text()="Имя" ]/parent::div/input')
    REGISTRATION_EMAIL = (By.XPATH, '//label[ text()="Email" ]/parent::div/input')
    REGISTRATION_PASSWORD = (By.XPATH, '//label[ text()="Пароль" ]/parent::div/input')
    REGISTRATION_BUTTON = (By.XPATH, './/button[text()='
                                     '"Зарегистрироваться"]')