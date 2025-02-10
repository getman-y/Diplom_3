from selenium.webdriver.common.by import By


class OrderPageLocators:
    ELEMENT_IN_ORDERS_LIST_BUTTON = By.XPATH, '//*[contains(@class, "OrderHistory_link")]'
    COMPOUND_IN_MODAL_DETAIL = By.XPATH, '//p[text()="Cостав"]'
    ORDER_ID = (By.XPATH, '//p[@class="text text_type_digits-default"]')
    TOTAL_ORDER_COUNT = (By.XPATH, "//p[text()='Выполнено за все время:']/following-sibling::p")
    DAILY_ORDER_COUNT = (By.XPATH, "//p[text()='Выполнено за сегодня:']/following-sibling::p")
    ORDER_ID_IN_PROGRESS = (By.XPATH, '//li[text()="{order_id}"]')
    ORDER_ID_IN_FEEDS =   (By.XPATH, '//p[text()="{order_id}"]')

