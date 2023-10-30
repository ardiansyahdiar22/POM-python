@feature_product @run
Feature: Product Page

@detail_product_page
Scenario: User able to see product detail page
    Given I open the browser 
    When I fill my "username/correct_username" with "field_username/text_field_uname"
    When I fill my "psswd/correct_password" with "field_password/text_field_password"
    When User click "login/btn_login"
    When User click "product/backpack_product"
    When User wait 3 seconds
    Then Element with "product/btn_add_to_card" is displayed
    Then Make sure text "price/product_price_regex " with element "product/price_product_detail" is displayed