from .base_page import BasePage
from selenium.webdriver.common.by import By

class MainPage(BasePage): # где BasePage наследник MainPage
    def go_to_login_page(browser): # указываем аргумент self, чтобы иметь доступ к атрибутам и методам класса
# Так как браузер у нас хранится как аргумент класса BasePage,обращаться к нему нужно соответствующим бразом с помощью self
        login_link = browser.find_element(By.CSS_SELECTOR, "#login_link")
        login_link.click()