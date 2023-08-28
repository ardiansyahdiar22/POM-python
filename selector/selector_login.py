from selenium.webdriver.common.by import By

class SelectorLogin:
    USERNAME_INPUT = (By.XPATH, '//*[@id="user-name"]')
    PASSWORD_INPUT = (By.XPATH, '//*[@id="password"]')
    LOGIN_BUTTON = (By.ID, 'login-button')