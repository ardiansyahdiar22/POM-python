from .base_page import BasePage
from selector.selector import SelectorWebApp
from selenium.webdriver.common.keys import Keys
from utils.config import Config

class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.selector_product = SelectorWebApp()

    def open(self):
        self.driver.get(Config.BASE_URL)
    
    def search_product(self, productName):
        search_product = self.wait_element_until_present(self.selector_product.SEARCH_BOX)
        search_product.send_keys(productName)
        search_product.send_keys(Keys.RETURN)
    
    def click_cardProduct(self):
        self.wait_element_until_present(self.selector_product.CARD_PRODUCT).click()
    
    def validate_imgProduct(self):
        self.wait_element_until_present(self.selector_product.IMG_PRODUCT).is_displayed()
    
    def click_shareProduct(self):
        self.wait_element_until_present(self.selector_product.BUTTON_SHARE).click()
    
    def click_loginBtn(self):
        self.wait_element_until_present(self.selector_product.BUTTON_LOGIN).click()
    
    def input_credential(self, email):
        formInput_email = self.wait_element_until_present(self.selector_product.FORM_INPUT_EMAIL)
        formInput_email.send_keys(email)
    
    def enable_btn(self):
        btnCheck = self.wait_element_until_present(self.selector_product.BUTTON_NEXT_LOGIN)
        return btnCheck.is_enabled()
