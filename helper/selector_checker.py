from selenium.webdriver.common.by import By
from utils.yaml_utils import YAMLUtils

class SelectorChecker:
    def __init__(self):
        self.selectors = YAMLUtils.load_yaml('./selector/selectors.yml')

    def find_selector(self, driver, selector_key):
        selector = self.selectors.get(selector_key)
        selector_type, selector_value = selector.split(':')

        if selector_type == 'xpath':
            return driver.find_element(By.XPATH, selector_value)
        elif selector_type == 'id':
            return driver.find_element(By.ID, selector_value)
        elif selector_type == 'css':
            return driver.find_element(By.CSS_SELECTOR, selector_value)
        elif selector_type == 'name':
            return driver.find_element(By.NAME, selector_value)
        else:
            print('Selector Not Found!!')