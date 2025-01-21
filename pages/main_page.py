from data import Urls
from locators.account_locators import AccountLocators
from locators.main_page_locators import MainPageLocators
from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):

    def go_to_constructor(self):
        self.go_to_url(Urls.FEED_URL)
        self.click_to_element(MainPageLocators.CONSTRUCT_BUTTON)
        self.find_element_with_wait(MainPageLocators.TITLE_MAIN_PAGE)

    def go_to_feeds(self):
        self.go_to_url(Urls.MAIN_URL)
        self.click_to_element(MainPageLocators.FEEDS_BUTTON)
        self.find_element_with_wait(OrderPageLocators.TOTAL_ORDER_COUNT)

    def go_to_account(self):
        self.click_to_element(MainPageLocators.BUTTON_ACCOUNT)
        self.find_element_with_wait(AccountLocators.BUTTON_PROFILE)

    def click_on_ingredients(self):
        self.go_to_url(Urls.MAIN_URL)
        self.click_to_element(MainPageLocators.INGREDIENTS_SNIPPET)
        self.find_element_with_wait(MainPageLocators.MODAL_WIH_DETAILS_INGREDIENTS)

    def click_on_modal_with_details_ingredients(self):
        text = self.get_text_from_element(MainPageLocators.MODAL_WIH_DETAILS_INGREDIENTS)
        return text

    def close_modal(self):
        self.click_to_element(MainPageLocators.CLOSE_MODAL_WIH_DETAILS_INGREDIENTS)
        text = self.get_text_from_element(MainPageLocators.TITLE_MAIN_PAGE)
        return text

    def check_counter_of_ingredients(self):
        self.find_element_with_wait(MainPageLocators.INGREDIENTS_COUNTER)
        counter = self.get_text_from_element(MainPageLocators.INGREDIENTS_COUNTER)
        return counter

    def drag_and_drop_ingredients(self):
        self.drag_and_drop(MainPageLocators.INGREDIENTS_SNIPPET, MainPageLocators.ORDER_SNIPPET)

    def click_button_create_order(self):
        self.find_element_with_wait(MainPageLocators.CREATE_ORDER_BUTTON)
        self.click_to_element(MainPageLocators.CREATE_ORDER_BUTTON)
        self.find_element_with_wait(MainPageLocators.ORDER_ID_TEXT)

    def return_order_id(self):
        id = self.get_text_from_element(MainPageLocators.ORDER_ID)
        while id == '9999':
            id = self.get_text_from_element(MainPageLocators.ORDER_ID)
        return f"0{id}"

    def return_order_id_text(self):
        self.find_element_with_wait(MainPageLocators.ORDER_ID_TEXT)
        text = self.get_text_from_element(MainPageLocators.ORDER_ID_TEXT)
        return text

    def create_order(self):
        self.go_to_constructor()
        self.drag_and_drop_ingredients()
        self.click_button_create_order()

