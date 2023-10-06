from selenium.webdriver.common.by import By

class SelectorWebApp:
    #SEARCH_BOX = (By.XPATH, '//input[@type="search"]')
    CARD_PRODUCT = (By.XPATH, '//div[@data-testid="master-product-card"]')
    IMG_PRODUCT = (By.XPATH, '//*[@data-testid="PDPMainImage"]')
    BUTTON_SHARE = (By.XPATH, '//*[@data-testid="pdpShareButton"]')

    ## Selector module Login ##
    ##BUTTON_LOGIN = (By.XPATH, '//*[@data-testid="btnHeaderLogin"]')
    #FORM_INPUT_EMAIL = (By.XPATH, '//*[@data-testid="email-phone-input"]')
    #BUTTON_NEXT_LOGIN = (By.XPATH, '//*[@data-testid="email-phone-submit"]')