from data import Urls, UserData
from locators.register_locators import RegisterLocators
from pages.base_page import BasePage
from pages.register_page import RegisterPage


class AuthPage(BasePage):
    def auth_user(self):
        register = RegisterPage()
        x = register.registration_user_and_return_data()
        print (x)


