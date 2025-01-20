from selenium.webdriver.common.by import By


class ResetPasswordLocators:
    CODE_INPUT= By.XPATH, '//label[text()="Введите код из письма"]/following-sibling::input'
    SHOW_PASSWORD_BUTTON = By.XPATH, '//div[contains(@class,"icon-action")]'
    INPUT_FOCUSED= By.CSS_SELECTOR, '.input__placeholder.input__placeholder-focused'



