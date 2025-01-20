from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):
    def check_counter(self):
        self.click_to_element(MainPageLocators.CONSTRUCT_BUTTON)

    def get_order_id(self):
        order_id = self.get_text_from_element(MainPageLocators.ORDER_ID)
        while order_id == '9999':
            order_id = self.get_text_from_element(MainPageLocators.ORDER_ID)
        return f"0{order_id}"
