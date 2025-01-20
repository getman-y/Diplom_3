import time

from data import Urls
from locators.account_locators import AccountLocators
from locators.auth_locators import AuthLocators
from locators.main_page_locators import MainPageLocators
from pages.main_page import MainPage
from pages.register_page import RegisterPage


class TestAccount:
    def test_redirect_to_account(self, driver):
        user = RegisterPage(driver)
        user.register_and_auth()
        main_page = MainPage(driver)
        main_page.click_to_element(MainPageLocators.BUTTON_ACCOUNT)
        main_page.find_element_with_wait(AccountLocators.BUTTON_PROFILE)
        assert main_page.current_url() == Urls.ACCOUNT_URL

    def test_redirect_to_history_of_orders(self, driver):
        user = RegisterPage(driver)
        user.register_and_auth()
        main_page = MainPage(driver)
        main_page.click_to_element(MainPageLocators.BUTTON_ACCOUNT)
        main_page.click_to_element(AccountLocators.HISTORY_OF_ORDER_BUTTON)
        assert main_page.current_url() == Urls.HISTORY_OR_ORDER_URL

    def test_logout_success(self, driver):
        user = RegisterPage(driver)
        user.register_and_auth()
        main_page = MainPage(driver)
        main_page.click_to_element(MainPageLocators.BUTTON_ACCOUNT)
        main_page.click_to_element(AccountLocators.BUTTON_LOGOUT)
        main_page.find_element_with_wait(AuthLocators.AUTH_BUTTON_EXIT)
        assert main_page.current_url() == Urls.LOGIN_URL