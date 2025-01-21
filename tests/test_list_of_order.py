from pages.account_page import AccountPage
from pages.history_page import HistoryPage
from pages.main_page import MainPage
from pages.orders_page import OrdersPage
from pages.register_page import RegisterPage


class TestListOfOrders:

    def test_show_orders_in_work_status(self, driver):
        user = RegisterPage(driver)
        user.register_and_auth()

        main_page = MainPage(driver)
        main_page.create_order()
        order_id = main_page.return_order_id()
        main_page.close_modal()

        orders_page = OrdersPage(driver)
        orders = orders_page.check_order_in_working()
        assert orders == order_id

    def test_show_details_order(self, driver):
        main_page = MainPage(driver)
        orders_page = OrdersPage(driver)

        main_page.go_to_feeds()
        is_find_element = orders_page.show_modal_with_details_order()
        assert is_find_element


    def test_show_orders_in_feeds_and_history (self, driver):
        user = RegisterPage(driver)
        user.register_and_auth()

        main_page = MainPage(driver)
        account_page = AccountPage(driver)
        history_page = HistoryPage(driver)
        order_page = OrdersPage(driver)

        main_page.create_order()
        main_page.close_modal()

        account_page.go_to_history_order()
        order_id_in_history = history_page.return_order_id()
        main_page.go_to_feeds()
        order_id_in_feeds = order_page.return_order_id()
        assert order_id_in_feeds == order_id_in_history

    def test_increase_counters_after_create_order(self, driver):
        user = RegisterPage(driver)
        user.register_and_auth()

        main_page = MainPage(driver)
        order_page = OrdersPage(driver)

        main_page.go_to_feeds()

        total_count_before = order_page.check_total_counter()
        day_count_before = order_page.check_day_counter()

        main_page.go_to_constructor()
        main_page.create_order()
        main_page.close_modal()
        main_page.go_to_feeds()

        total_count_after = order_page.check_total_counter()
        day__count_after = order_page.check_day_counter()
        assert total_count_after > total_count_before and day__count_after > day_count_before
