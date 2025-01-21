import allure

from data import Urls
from pages.account_page import AccountPage
from pages.main_page import MainPage
from pages.register_page import RegisterPage


class TestAccount:

    @allure.title('Проверка перехода по клику на «Личный кабинет»')
    def test_redirect_to_account(self, driver):
        user = RegisterPage(driver)
        user.register_and_auth()
        main_page = MainPage(driver)
        main_page.go_to_account()
        assert main_page.current_url() == Urls.ACCOUNT_URL

    @allure.title('Проверка перехода по клику на «История заказов»')
    def test_redirect_to_history_of_orders(self, driver):
        user = RegisterPage(driver)
        user.register_and_auth()

        account_page = AccountPage(driver)
        account_page.go_to_history_order()
        assert account_page.current_url() == Urls.HISTORY_OR_ORDER_URL

    @allure.title('Проверка успешного выхода из ЛК')
    def test_logout_success(self, driver):
        user = RegisterPage(driver)
        user.register_and_auth()

        account_page = AccountPage(driver)
        account_page.logout()
        assert account_page.current_url() == Urls.LOGIN_URL