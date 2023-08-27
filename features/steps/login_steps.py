from behave import given, when, then
from pages.login_page import LoginPage
from utils.webdriver_utils import WebDriverUtils
import time

@given('I am on the login page')
def step_impl(context):
    context.driver = WebDriverUtils.create_driver()
    context.login_page = LoginPage(context.driver)
    context.login_page.open()

@when('I enter my "{username}" and "{password}"')
def step_impl(context, username, password):
    time.sleep(4)
    context.login_page.enter_credentials(username, password)

@when('I click the login button')
def step_impl(context):
    time.sleep(5)
    context.login_page.click_login_button()

@then('I should be redirected to the dashboard')
def step_impl(context):
    time.sleep(4)
    elementTxt = context.login_page.dashboard_title()
    print(elementTxt)
    assert "Products" in elementTxt
    context.driver.quit()
