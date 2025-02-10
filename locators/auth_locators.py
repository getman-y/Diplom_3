from selenium.webdriver.common.by import By


class AuthLocators:
    AUTH_BUTTON_EXIT = (By.XPATH, './/button[text()="Войти"]')
    RECOVERY_PASSWORD_BUTTON = (By.XPATH, '//a[contains(@href, "/forgot-password")]')