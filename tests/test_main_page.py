from data import Urls
from pages.main_page import MainPage
from pages.register_page import RegisterPage


class TestMainPage:

    def test_click_button_construct_show_main_page(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_constructor()
        assert main_page.current_url() == Urls.MAIN_URL

    def test_click_button_feeds_show_feeds_page(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_feeds()
        assert main_page.current_url() == Urls.FEED_URL

    def test_click_ingredients_show_modal_page(self, driver):
        main_page = MainPage(driver)
        main_page.click_on_ingredients()
        text = main_page.click_on_modal_with_details_ingredients()
        assert text == 'Детали ингредиента'

    def test_click_button_close_in_modal(self, driver):
        main_page = MainPage(driver)
        main_page.click_on_ingredients()
        check = main_page.close_modal()
        assert check == 'Соберите бургер'

    def test_increase_counter_after_add_ingredient(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_constructor()
        counter_before_add = main_page.check_counter_of_ingredients()
        main_page.drag_and_drop_ingredients()
        counter_after_add = main_page.check_counter_of_ingredients()
        assert counter_after_add > counter_before_add

    def test_auth_user_create_order_success(self, driver):
        reg_page = RegisterPage(driver)
        reg_page.register_and_auth()

        main_page = MainPage(driver)
        main_page.click_button_create_order()
        text = main_page.return_order_id_text()
        assert text == 'идентификатор заказа'



