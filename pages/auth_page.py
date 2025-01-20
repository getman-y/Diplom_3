from data import Urls, UserData
from locators.register_locators import RegisterLocators
from pages.base_page import BasePage
from pages.register_page import RegisterPage


class AuthPage(BasePage):
    def current_url(self):
        return self.driver.current_url




