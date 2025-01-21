from locators.account_locators import AccountLocators
from locators.auth_locators import AuthLocators
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class AccountPage(BasePage):
    def go_to_history_order(self):
        self.click_to_element(MainPageLocators.BUTTON_ACCOUNT)
        self.find_element_with_wait(AccountLocators.BUTTON_PROFILE)
        self.click_to_element(AccountLocators.HISTORY_OF_ORDER_BUTTON)

    def logout(self):
        self.click_to_element(MainPageLocators.BUTTON_ACCOUNT)
        self.find_element_with_wait(AccountLocators.BUTTON_PROFILE)
        self.click_to_element(AccountLocators.BUTTON_LOGOUT)
        self.find_element_with_wait(AuthLocators.AUTH_BUTTON_EXIT)

