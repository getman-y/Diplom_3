from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):
    def check_counter(self):
        self.click_to_element(MainPageLocators.CONSTRUCT_BUTTON)