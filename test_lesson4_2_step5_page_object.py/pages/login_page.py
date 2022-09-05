from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert login_url == True, "login_url not found!"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert login_form == True, "login_form not found!"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert register_form == True, "register_form not found!"
