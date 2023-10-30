from .base_page import BasePage
from selenium.webdriver.common.keys import Keys
from utils.config import Config
from helper.selector_checker import SelectorChecker
from helper.copy_helper import HelpergetCopy
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.implicitly_wait(15)
        self.selector_help = SelectorChecker()
        self.copy_helper = HelpergetCopy()

    def open(self):
        self.driver.get(Config.BASE_URL_SAUCE_DEMO)

####################################################
## Function for Behaviour tap Enter on keyboard ##
####################################################
    def click_enter(self, selector_key):
        actionEnter = self.selector_help.find_selector(self.driver, selector_key)
        actionEnter.send_keys(Keys.RETURN)

#############################################################################
## Function for fill text field {Example fill username & pasword for login ##
#############################################################################
    def fill_textField(self, user_key, selector_key):
        input_selector = self.selector_help.find_selector(self.driver, selector_key)
        input_text = self.copy_helper.get_copy(user_key)

        input_selector.send_keys(input_text)

####################################################
## Function for validation button enable ##
####################################################
    def check_validateButton(self, selector_key):
        btnCheck = self.selector_help.find_selector(self.driver, selector_key)
        return btnCheck.is_enabled()

####################################################
## Function for Behaviour click button ##
####################################################
    def click_action(self, selector_key):
        selector = self.selector_help.find_selector(self.driver, selector_key)
        print(f'Selector : {selector}')

        try:
            selector.click()
            print("Element successfully clicked.")
        except Exception as e:
            print(f"Error occurred: {e}")

    def validate_equals(self, selector_key, key_text):
        selector = self.selector_help.find_selector(selector_key)
        get_text = self.copy_helper.get_copy(key_text)

        get_element = self.driver.find_element(By.XPATH, selector)
        element_text = get_element.text

        print(element_text)
        
        try:
            assert element_text == get_text, f"Element expected"
        except Exception as e:
            print(f"Not same assertion text: {e}")

####################################################
## Function for check text or copy displayed ##
####################################################
    def displayed_copy(self, user_key, selector_key):
        text_get = self.copy_helper.get_copy(user_key)
        get_element = self.selector_help.find_selector(self.driver, selector_key)
        
        try:
            return get_element.is_displayed()
        except Exception as e:
            print(f"Element with copy not found {e}")

####################################################
## Function for check element is displayed ##
####################################################
    def element_displayed(self, selector_key):
        element_get = self.selector_help.find_selector(self.driver, selector_key)

        try:
            return element_get.is_displayed()
        except Exception as e:
            print(f"Element is not displayed{e}")