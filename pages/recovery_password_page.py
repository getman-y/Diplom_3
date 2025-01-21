from data import Urls, UserData
from locators.auth_locators import AuthLocators
from locators.forgot_password_locators import ForgotPasswordLocators
from locators.reset_password_locators import ResetPasswordLocators
from pages.base_page import BasePage


class RecoveryPasswordPage(BasePage):
    def go_to_login(self):
        self.go_to_url(Urls.LOGIN_URL)

    def click_recovery_password_button(self):
        self.click_to_element(AuthLocators.RECOVERY_PASSWORD_BUTTON)
        self.find_element_with_wait(ForgotPasswordLocators.RECOVERY_PASSWORD_BUTTON)

    def input_email(self):
        user_data = UserData.user_data_for_register()
        self.find_element_with_wait(AuthLocators.RECOVERY_PASSWORD_BUTTON)
        self.click_to_element(AuthLocators.RECOVERY_PASSWORD_BUTTON)
        self.add_text_to_element(ForgotPasswordLocators.EMAIL_INPUT, user_data[0])

    def click_recovery_button(self):
        self.click_to_element(ForgotPasswordLocators.RECOVERY_PASSWORD_BUTTON)
        self.find_element_with_wait(ResetPasswordLocators.CODE_INPUT)


    def input_email_and_click_recovery(self):
        self.go_to_login()
        self.input_email()
        self.click_recovery_button()

    def click_show_password_button(self):
        self.find_element_with_wait(ResetPasswordLocators.SHOW_PASSWORD_BUTTON)
        self.click_to_element(ResetPasswordLocators.SHOW_PASSWORD_BUTTON)

    def check_focused_field(self):
        if self.find_element_with_wait(ResetPasswordLocators.INPUT_FOCUSED):
            return True





