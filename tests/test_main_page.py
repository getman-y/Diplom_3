from data import Urls
from locators.main_page_locators import MainPageLocators
from pages.main_page import MainPage
from pages.register_page import RegisterPage


class TestMainPage:

    def test_click_button_construct_show_main_page(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_url(Urls.FEED_URL)
        main_page.click_to_element(MainPageLocators.CONSTRUCT_BUTTON)
        assert main_page.current_url() == Urls.MAIN_URL

    def test_click_button_feeds_show_feeds_page(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_url(Urls.MAIN_URL)
        main_page.click_to_element(MainPageLocators.FEEDS_BUTTON)
        assert main_page.current_url() == Urls.FEED_URL

    def test_click_bun_show_modal_page(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_url(Urls.MAIN_URL)
        main_page.click_to_element(MainPageLocators.BUN_SNIPPET)
        text = main_page.get_text_from_element(MainPageLocators.MODAL_WIH_DETAILS_INGREDIENTS)
        assert text == 'Детали ингредиента'

    def test_click_close_in_modal_close_modal(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_url(Urls.MAIN_URL)
        main_page.click_to_element(MainPageLocators.BUN_SNIPPET)
        main_page.find_element_with_wait(MainPageLocators.MODAL_WIH_DETAILS_INGREDIENTS)
        main_page.click_to_element(MainPageLocators.CLOSE_MODAL_WIH_DETAILS_INGREDIENTS)
        text = main_page.get_text_from_element(MainPageLocators.TITLE_MAIN_PAGE)
        assert text == 'Соберите бургер'

    def test_increase_counter_after_add_ingredient(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_url(Urls.MAIN_URL)
        counter_before_add = main_page.get_text_from_element(MainPageLocators.INGREDIENTS_COUNTER)
        main_page.drag_and_drop(MainPageLocators.BUN_SNIPPET, MainPageLocators.ORDER_SNIPPET)
        counter_after_add = main_page.get_text_from_element(MainPageLocators.INGREDIENTS_COUNTER)
        assert counter_after_add > counter_before_add

    def test_auth_user_create_order_success(self, driver):
        reg_page = RegisterPage(driver)
        reg_page.register_and_auth()
        main_page = MainPage(driver)
        main_page.click_to_element(MainPageLocators.CREATE_ORDER_BUTTON)
        text = main_page.get_text_from_element(MainPageLocators.ORDER_ID_TEXT)
        assert text == 'идентификатор заказа'



