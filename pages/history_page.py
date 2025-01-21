from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage


class HistoryPage(BasePage):

    def return_order_id(self):
        id = self.get_text_from_element(OrderPageLocators.ORDER_ID)
        return id