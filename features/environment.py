from utils.webdriver_utils import WebDriverUtils

def before_all(context):
    context.driver = WebDriverUtils.create_driver()

def after_all(context, driver):
    context.driver = WebDriverUtils.quit_driver(driver)