from selenium import webdriver

class WebDriverUtils:
    def create_driver():
        driver = webdriver.Chrome()
        driver.maximize_window()
        return driver

    def quit_driver(driver):
        driver.quit()
