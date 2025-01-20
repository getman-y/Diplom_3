from selenium.webdriver.common.by import By


class OrderPageLocators:
    ELEMENT_IN_ORDERS_LIST_BUTTON = By.XPATH, '//*[contains(@class, "OrderHistory_link")]'
    COMPOUND_IN_MODAL_DETAIL = By.XPATH, '//p[text()="Cостав"]'
    ORDER_ID = (By.XPATH, '//p[@class="text text_type_digits-default"]')
    TOTAL_ORDER_COUNT = (By.XPATH, "//p[text()='Выполнено за все время:']/following-sibling::p")
    ALL_ORDERS_AT_HISTORY = (By.XPATH, '//p[@class="text text_type_digits-default"]')
    DAILY_ORDER_COUNT = (By.XPATH, "//p[text()='Выполнено за сегодня:']/following-sibling::p")
    NUMBER_IN_PROGRESS = (By.XPATH, '//ul[2]/li[1][@class="text text_type_digits-default mb-2"]')