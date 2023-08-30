from .base_page import BasePage
from selector.selector_login import SelectorLogin

class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.selector_login = SelectorLogin()

    def open(self, url):
        self.driver.get(url)

    def enter_credentials(self, username, password):
        self.wait_for_element(self.selector_login.USERNAME_INPUT).send_keys(username)
        self.wait_for_element(self.selector_login.PASSWORD_INPUT).send_keys(password)

    def click_login_button(self):
        self.wait_for_element(self.selector_login.LOGIN_BUTTON).click()
