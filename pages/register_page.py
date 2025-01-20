import time

from data import Urls, UserData
from locators.auth_locators import AuthLocators
from locators.main_page_locators import MainPageLocators
from locators.register_locators import RegisterLocators
from pages.base_page import BasePage


class RegisterPage(BasePage):
    def register_and_auth(self):
        user_data = UserData.user_data_for_register()
        self.go_to_url(Urls.REGISTER_URL)
        self.find_element_with_wait(RegisterLocators.REGISTRATION_NAME).send_keys(user_data[2])
        self.find_element_with_wait(RegisterLocators.REGISTRATION_EMAIL).send_keys(user_data[0])
        self.find_element_with_wait(RegisterLocators.REGISTRATION_PASSWORD).send_keys(user_data[1])
        self.click_to_element(RegisterLocators.REGISTRATION_BUTTON)
        self.find_element_with_wait(AuthLocators.AUTH_BUTTON_EXIT)
        self.find_element_with_wait(RegisterLocators.REGISTRATION_EMAIL).send_keys(user_data[0])
        self.find_element_with_wait(RegisterLocators.REGISTRATION_PASSWORD).send_keys(user_data[1])
        self.click_to_element(AuthLocators.AUTH_BUTTON_EXIT)
        self.find_element_with_wait(MainPageLocators.TITLE_MAIN_PAGE)

