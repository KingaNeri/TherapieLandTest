from pages.login.login_page import LoginPage
import config.config as config


class LoginPageActions:
    def __init__(self, driver):
        self.driver = driver
        self.login_page = LoginPage(driver)

    def load(self):
        self.driver.get(config.LOGIN_PAGE)

    def fill_email_input(self, email):
        self.login_page.email_input.web_element.send_keys(email)

    def fill_password_input(self, password):
        self.login_page.password_input.web_element.send_keys(password)

    def click_login_button(self):
        self.login_page.login_button.web_element.click()
