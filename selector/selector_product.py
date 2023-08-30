from selenium.webdriver.common.by import By

class SelectorProduct:
    SEARCH_BOX = (By.XPATH, '//input[@type="search"]')
    CARD_PRODUCT = (By.XPATH, '//div[@data-testid="master-product-card"]')
    IMG_PRODUCT = (By.XPATH, '//*[@data-testid="PDPMainImage"]')