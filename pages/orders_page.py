from data import Urls
from locators.main_page_locators import MainPageLocators
from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage


class OrdersPage(BasePage):
    def check_order_in_working(self, id):
        self.go_to_url(Urls.MAIN_URL)
        self.click_to_element(MainPageLocators.FEEDS_BUTTON)
        locator= (OrderPageLocators.ORDER_ID_IN_PROGRESS[0], OrderPageLocators.ORDER_ID_IN_PROGRESS[1].format(order_id=id))
        print(locator)
        if self.find_element_with_wait(locator):
            return True

    def show_modal_with_details_order(self):
        self.find_element_with_wait(OrderPageLocators.ELEMENT_IN_ORDERS_LIST_BUTTON)
        self.click_to_element(OrderPageLocators.ELEMENT_IN_ORDERS_LIST_BUTTON)
        if self.find_element_with_wait(OrderPageLocators.COMPOUND_IN_MODAL_DETAIL):
            return True


    def check_id_in_feed_page(self, id):
        locator= (OrderPageLocators.ORDER_ID_IN_FEEDS[0], OrderPageLocators.ORDER_ID_IN_FEEDS[1].format(order_id=id))
        if self.find_element_with_wait(locator):
            return True


    def check_total_counter(self):
        counter = self.get_text_from_element(OrderPageLocators.TOTAL_ORDER_COUNT)
        return counter

    def check_day_counter(self):
        counter = self.get_text_from_element(OrderPageLocators.DAILY_ORDER_COUNT)
        return counter