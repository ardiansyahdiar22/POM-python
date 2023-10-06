@feature_product @run
Feature: Search product

@searching_the_product
Scenario: Verify user able to search product
    Given I open the browser 
    When I fill my "product/name_product" with "search_textField/input_name_product"
    When User click enter with "search_textField/input_name_product"
    When User wait 5 seconds
    Then Verify element "title_all/text_title_all_product" equals with "title/expected_txt_title"
    # Then I can see product detail page

# @share_product
# Scenario Outline: Verify user able to share the product
#     Given I open the browser
#     When I type product name "<productName>" and click enter
#     When I click card product
#     Then I can click share button

#     Examples:
#         | productName | 
#         | ponds men | 