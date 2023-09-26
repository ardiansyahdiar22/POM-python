from behave import *
from utils.webdriver_utils import WebDriverUtils
from selenium.webdriver.common.by import By
import time
from pages.main_page import MainPage

@given('I open the browser')
def step_openBrowser(context):
    context.driver = WebDriverUtils.create_driver()
    context.main_page = MainPage(context.driver)
    context.main_page.open()

@when('I enter my "{email}"')
def step_inputEmail(context, email):
    context.main_page.input_credential(email)
    time.sleep(2)

@when('User click button login')
def step_clickLogin(context):
    context.main_page.click_loginBtn()
    time.sleep(1)

@then('Button login is enabled')
def step_validateBtn(context):
    is_enabled = context.main_page.enable_btn()
    assert is_enabled, "Button not disabled"

############################
## Steps Search Product ##
############################

@when('I type product name "{productName}" and click enter')
def step_searchProduct(context, productName):
    context.main_page.search_product(productName)

@when('I click card product')
def step_clickCard(context):
    context.main_page.click_cardProduct()

@then('I can see product detail page')
def step_pdpPage(context):
    time.sleep(5)
    context.main_page.validate_imgProduct() 

@then('I can click share button')
def click_share_btn(context):
    context.main_page.click_shareProduct()
    time.sleep(3)
