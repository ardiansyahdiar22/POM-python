from .base_page import BasePage
from selector.selector_product import SelectorProduct
from selenium.webdriver.common.keys import Keys

class ProductPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.selector_product = SelectorProduct()

    def open(self, url):
        self.driver.get(url)
    
    def search_product(self, productName):
        search_product = self.wait_element_until_present(self.selector_product.SEARCH_BOX)
        search_product.send_keys(productName)
        search_product.send_keys(Keys.RETURN)
    
    def click_cardProduct(self):
        self.wait_element_until_present(self.selector_product.CARD_PRODUCT).click()
    
    def validate_imgProduct(self):
        self.wait_element_until_present(self.selector_product.IMG_PRODUCT).is_displayed()
