from behave import *
from utils.webdriver_utils import WebDriverUtils
import time
from pages.main_page import MainPage

@given('I open the browser')
def step_openBrowser(context):
    context.driver = WebDriverUtils.create_driver()
    context.main_page = MainPage(context.driver)
    context.main_page.open()

@when('User click "{selector_key}"')
def step_clickAction(context, selector_key):
    context.main_page.click_action(selector_key)

@when('I fill my "{user_key}" with "{selector_key}"')
def step_fill(context, user_key, selector_key):
    context.main_page.fill_textField(user_key, selector_key)

@when('User wait {seconds} seconds')
def wait_for_seconds(context, seconds):
    time.sleep(int(seconds))

@then('"{selector_key}" is enabled')
def step_validateBtn(context, selector_key):
    is_enabled = context.main_page.check_validateButton(selector_key)
    assert is_enabled, "Button not disabled"

@then('Make sure text "{user_key}" with element "{selector_key}" is displayed')
def validate_textDisplay(context, user_key, selector_key):
    context.main_page.displayed_copy(user_key, selector_key)

@then('Element with "{selector_key}" is displayed')
def validate_elementDisplayed(context, selector_key):
    context.main_page.element_displayed(selector_key)

############################
## Steps Search Product ##
############################

@when('User click enter with "{selector_key}"')
def tap_enter(context, selector_key):
    context.main_page.click_enter(selector_key)

@then('Verify element "{selector_key}" equals with "{key_text}"')
def validate_assert(context, selector_key, key_text):
    context.main_page.validate_equals(selector_key, key_text)