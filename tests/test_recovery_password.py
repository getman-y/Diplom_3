from data import Urls
from locators.reset_password_locators import ResetPasswordLocators
from pages.recovery_password_page import RecoveryPasswordPage


class TestRecoveryPassword:
    def test_redirect_recovery_button(self, driver):
        recovery_page = RecoveryPasswordPage(driver)
        recovery_page.go_to_login()
        recovery_page.click_recovery_password_button()
        assert recovery_page.current_url() == Urls.FORGOT_PASSWORD_URL

    def test_input_email_and_click_button(self, driver):
        recovery_page = RecoveryPasswordPage(driver)
        recovery_page.input_email_and_click_recovery()
        assert recovery_page.current_url() == Urls.RESET_PASSWORD_URL

    def test_made_input_active(self, driver):
        recovery_page = RecoveryPasswordPage(driver)
        recovery_page.input_email_and_click_recovery()
        recovery_page.click_to_element(ResetPasswordLocators.SHOW_PASSWORD_BUTTON)
        is_find_element = recovery_page.check_focused_field()
        assert is_find_element