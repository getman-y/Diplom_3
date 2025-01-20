from selenium.webdriver.common.by import By


class AccountLocators:
    BUTTON_PROFILE = (By.XPATH, './/a[text()="Профиль"]')
    HISTORY_OF_ORDER_BUTTON = (By.XPATH, './/a[text()="История заказов"]')
    BUTTON_LOGOUT = (By.XPATH, './/button[text()="Выход"]')
