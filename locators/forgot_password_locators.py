from selenium.webdriver.common.by import By


class ForgotPasswordLocators:
    RECOVERY_PASSWORD_BUTTON = By.XPATH, '//button[text()="Восстановить"]'
    EMAIL_INPUT= By.XPATH, '//label[text()="Email"]/following-sibling::input'