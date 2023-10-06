from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 25)
    
    def wait_element_until_present(self, selector_key):
        return self.wait.until(EC.presence_of_element_located(selector_key))
