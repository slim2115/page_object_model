from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException # Добавим иссключение

class BasePage():
    def __init__(self, browser, url, timeout=10):
        self.browser: webdriver = browser
        self.url = url
        self.browser.implicitly_wait(timeout)  # команда для неявного ожидания
    def open(self):
       self.browser.get(self.url)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True