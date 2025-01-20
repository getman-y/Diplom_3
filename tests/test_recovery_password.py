import time

from data import Urls, UserData
from locators.auth_locators import AuthLocators
from locators.forgot_password_locators import ForgotPasswordLocators
from locators.reset_password_locators import ResetPasswordLocators
from pages.auth_page import AuthPage


class TestRecoveryPassword:
    def test_redirect_recovery_button(self, driver):
        login_page = AuthPage(driver)
        login_page.go_to_url(Urls.LOGIN_URL)
        login_page.click_to_element(AuthLocators.RECOVERY_PASSWORD_BUTTON)
        login_page.find_element_with_wait(ForgotPasswordLocators.RECOVERY_PASSWORD_BUTTON)
        assert login_page.current_url() == Urls.FORGOT_PASSWORD_URL

    def test_input_email_and_click_button(self, driver):
        user_data = UserData.user_data_for_register()
        login_page = AuthPage(driver)
        login_page.go_to_url(Urls.LOGIN_URL)
        login_page.click_to_element(AuthLocators.RECOVERY_PASSWORD_BUTTON)
        login_page.find_element_with_wait(ForgotPasswordLocators.RECOVERY_PASSWORD_BUTTON)
        login_page.add_text_to_element(ForgotPasswordLocators.EMAIL_INPUT, user_data[0])
        login_page.click_to_element(ForgotPasswordLocators.RECOVERY_PASSWORD_BUTTON)
        login_page.find_element_with_wait(ResetPasswordLocators.CODE_INPUT)
        assert login_page.current_url() == Urls.RESET_PASSWORD_URL

    def test_made_input_active(self, driver):
        user_data = UserData.user_data_for_register()
        login_page = AuthPage(driver)
        login_page.go_to_url(Urls.LOGIN_URL)
        login_page.click_to_element(AuthLocators.RECOVERY_PASSWORD_BUTTON)
        login_page.find_element_with_wait(ForgotPasswordLocators.RECOVERY_PASSWORD_BUTTON)
        login_page.add_text_to_element(ForgotPasswordLocators.EMAIL_INPUT, user_data[0])
        login_page.click_to_element(ForgotPasswordLocators.RECOVERY_PASSWORD_BUTTON)
        login_page.find_element_with_wait(ResetPasswordLocators.CODE_INPUT)
        login_page.click_to_element(ResetPasswordLocators.SHOW_PASSWORD_BUTTON)
        login_page.find_element_with_wait(ResetPasswordLocators.INPUT_FOCUSED)