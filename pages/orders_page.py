from data import Urls
from locators.main_page_locators import MainPageLocators
from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage


class OrdersPage(BasePage):
    def check_order_in_working(self):
        self.go_to_url(Urls.MAIN_URL)
        self.click_to_element(MainPageLocators.FEEDS_BUTTON)
        self.find_element_with_wait(OrderPageLocators.TOTAL_ORDER_COUNT)
        text = self.get_text_from_element(OrderPageLocators.NUMBER_IN_PROGRESS)
        return text

    def show_modal_with_details_order(self):
        self.find_element_with_wait(OrderPageLocators.ELEMENT_IN_ORDERS_LIST_BUTTON)
        self.click_to_element(OrderPageLocators.ELEMENT_IN_ORDERS_LIST_BUTTON)
        if self.find_element_with_wait(OrderPageLocators.COMPOUND_IN_MODAL_DETAIL):
            return True

    def return_order_id(self):
        self.find_element_with_wait(OrderPageLocators.TOTAL_ORDER_COUNT)
        id = self.get_text_from_element(OrderPageLocators.ALL_ORDERS_AT_HISTORY)
        return id

    def check_total_counter(self):
        counter = self.get_text_from_element(OrderPageLocators.TOTAL_ORDER_COUNT)
        return counter

    def check_day_counter(self):
        counter = self.get_text_from_element(OrderPageLocators.DAILY_ORDER_COUNT)
        return counter