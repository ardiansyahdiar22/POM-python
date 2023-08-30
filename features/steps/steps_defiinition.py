from behave import *
from pages.login_page import LoginPage
from utils.webdriver_utils import WebDriverUtils
from selenium.webdriver.common.by import By
import time
from pages.product_page import ProductPage

@given('I open the browser with "{url}"')
def step_openBrowser(context, url):
    context.driver = WebDriverUtils.create_driver()
    context.product_page = ProductPage(context.driver)
    context.product_page.open(url)

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

############################
## Steps Search Product ##
############################

@when('I type product name "{productName}" and click enter')
def step_searchProduct(context, productName):
    context.product_page.search_product(productName)

@when('I click card product')
def step_clickCard(context):
    context.product_page.click_cardProduct()

@then('I can see product detail page')
def step_pdpPage(context):
    time.sleep(5)
    context.product_page.validate_imgProduct()
