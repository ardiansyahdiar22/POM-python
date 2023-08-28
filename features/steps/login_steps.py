from behave import given, when, then
from pages.login_page import LoginPage
from utils.webdriver_utils import WebDriverUtils
from selenium.webdriver.common.by import By
import time

@given('I am on the login page')
def step_openBrowser(context):
    context.driver = WebDriverUtils.create_driver()
    context.login_page = LoginPage(context.driver)
    context.login_page.open()

@when('I enter my "{username}" and "{password}"')
def step_inputUnamePsswd(context, username, password):
    context.login_page.enter_credentials(username, password)

@when('I click the login button')
def step_clickLogin(context):
    context.login_page.click_login_button()

@then('I should be redirected to the dashboard')
def step_directToDashboard(context):
    time.sleep(3)
    elementTxt = context.driver.find_element(By.XPATH, '//*[@class="title"]').text
    assert "Products" in elementTxt