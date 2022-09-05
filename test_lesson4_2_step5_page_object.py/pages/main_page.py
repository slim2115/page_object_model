from .base_page import BasePage
from .locators import MainPageLocators
from .login_page import LoginPage
from selenium.webdriver.common.by import By

class MainPage(BasePage): # где BasePage наследник MainPage
    def go_to_login_page(self, browser):    # указываем аргумент self, чтобы иметь доступ к атрибутам и методам класса
# Так как браузер у нас хранится как аргумент класса BasePage,обращаться к нему нужно соответствующим бразом с помощью self
        login_link = browser.find_element(By.CSS_SELECTOR, "#login_link")
        login_link.click()
    def should_be_login_link(self):
# Хорошая практика: писать сначала красные тесты и только потом делать их зелеными
        assert self.is_element_present(By.CSS_SELECTOR, "#login_link")

    def go_to_login_page(self):
        link = self.browser.find_element(*MainPageLocators.LOGIN_LINK) # Добавим кортеж по селекторам с точки зрения тест-дизайна
        link.click()
        # return LoginPage(browser=self.browser, url=self.browser.current_url)


