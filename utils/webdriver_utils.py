from selenium import webdriver

class WebDriverUtils:
    def create_driver():
        driver = webdriver.Chrome()  # Ganti dengan driver yang sesuai (misalnya Firefox)
        return driver
