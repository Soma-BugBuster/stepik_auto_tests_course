from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert self.check_part_of_url('login')

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Sign in form not found"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.SIGN_UP_FORM), "Sign up form not found"
