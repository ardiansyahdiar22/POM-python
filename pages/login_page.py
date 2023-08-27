from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get("https://www.saucedemo.com/")

    def enter_credentials(self, username, password):
        self.driver.find_element(By.XPATH, '//*[@id="user-name"]').send_keys(username)
        self.driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(password)

    def click_login_button(self):
        self.driver.find_element(By.ID, "login-button").click()
    
    def dashboard_title(self):
        return self.driver.find_element(By.XPATH, '//*[@class="title"]').text
