from selenium.webdriver.common.by import By


class MainPageLocators():
 LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():

    def should_be_login_url(self, browser):
        login_url = browser.find_element(By.ID, "#id_login-redirect_url")
        login_url.click()

    def should_be_login_form(self, browser):
        login_form = browser.find_element(By.ID, "#login_form")
        login_form.click()

    def should_be_register_form(self, browser):
        register_form = browser.find_element(By.ID, "#register_form")
        register_form.click()


