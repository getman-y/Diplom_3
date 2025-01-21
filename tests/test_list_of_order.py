from data import Urls
from locators.account_locators import AccountLocators
from locators.main_page_locators import MainPageLocators
from locators.order_page_locators import OrderPageLocators
from pages.main_page import MainPage
from pages.register_page import RegisterPage


class TestListOfOrders:

    def test_show_orders_in_work_status(self, driver):
        user = RegisterPage(driver)
        user.register_and_auth()
        main_page = MainPage(driver)
        main_page.go_to_url(Urls.MAIN_URL)
        main_page.drag_and_drop(MainPageLocators.INGREDIENTS_SNIPPET, MainPageLocators.ORDER_SNIPPET)
        main_page.click_to_element(MainPageLocators.CREATE_ORDER_BUTTON)
        order_id = main_page.get_order_id()
        main_page.close_modal()
        main_page.click_with_wait_clickable(MainPageLocators.FEEDS_BUTTON)
        main_page.find_element_with_wait(OrderPageLocators.TOTAL_ORDER_COUNT)
        orders = main_page.get_text_from_element(OrderPageLocators.NUMBER_IN_PROGRESS)
        assert orders == order_id

    # def test_show_details_order(self, driver):
    #     main_page = MainPage(driver)
    #     main_page.go_to_url(Urls.MAIN_URL)
    #     main_page.click_to_element(MainPageLocators.FEEDS_BUTTON)
    #     main_page.find_element_with_wait(OrderPageLocators.ELEMENT_IN_ORDERS_LIST_BUTTON)
    #     main_page.click_to_element(OrderPageLocators.ELEMENT_IN_ORDERS_LIST_BUTTON)
    #     is_find_element = main_page.find_element_with_wait(OrderPageLocators.COMPOUND_IN_MODAL_DETAIL)
    #     assert is_find_element
    #
    # def test_show_orders_in_feeds (self, driver):
    #     user = RegisterPage(driver)
    #     user.register_and_auth()
    #     main_page = MainPage(driver)
    #     main_page.go_to_url(Urls.MAIN_URL)
    #     main_page.drag_and_drop(MainPageLocators.INGREDIENTS_SNIPPET, MainPageLocators.ORDER_SNIPPET)
    #     main_page.click_to_element(MainPageLocators.CREATE_ORDER_BUTTON)
    #     main_page.click_with_wait_clickable(MainPageLocators.CLOSE_MODAL_BUTTON)
    #     main_page.click_with_wait_clickable(MainPageLocators.BUTTON_ACCOUNT)
    #     main_page.click_with_wait_clickable(AccountLocators.HISTORY_OF_ORDER_BUTTON)
    #     order_number_in_history = main_page.get_text_from_element(OrderPageLocators.ORDER_ID)
    #     main_page.click_to_element(MainPageLocators.FEEDS_BUTTON)
    #     main_page.find_element_with_wait(OrderPageLocators.TOTAL_ORDER_COUNT)
    #     order_number_in_feeds = main_page.get_text_from_element(OrderPageLocators.ALL_ORDERS_AT_HISTORY)
    #     assert order_number_in_feeds == order_number_in_history
    #
    # def test_increase_counters_after_create_order(self, driver):
    #     user = RegisterPage(driver)
    #     user.register_and_auth()
    #     main_page = MainPage(driver)
    #     main_page.go_to_url(Urls.MAIN_URL)
    #     main_page.click_to_element(MainPageLocators.FEEDS_BUTTON)
    #     total_count = main_page.get_text_from_element(OrderPageLocators.TOTAL_ORDER_COUNT)
    #     day_count = main_page.get_text_from_element(OrderPageLocators.DAILY_ORDER_COUNT)
    #     main_page.go_to_url(Urls.MAIN_URL)
    #     main_page.drag_and_drop(MainPageLocators.INGREDIENTS_SNIPPET, MainPageLocators.ORDER_SNIPPET)
    #     main_page.click_to_element(MainPageLocators.CREATE_ORDER_BUTTON)
    #     main_page.click_with_wait_clickable(MainPageLocators.CLOSE_MODAL_BUTTON)
    #     main_page.click_with_wait_clickable(MainPageLocators.FEEDS_BUTTON)
    #     total_after = main_page.get_text_from_element(OrderPageLocators.TOTAL_ORDER_COUNT)
    #     day_after = main_page.get_text_from_element(OrderPageLocators.DAILY_ORDER_COUNT)
    #     assert total_after > total_count and day_after > day_count
