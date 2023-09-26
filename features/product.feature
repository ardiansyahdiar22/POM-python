@feature_product @run
Feature: Search product

@searching_the_product
Scenario Outline: Verify user able to search product
    Given I open the browser 
    When I type product name "<productName>" and click enter
    When I click card product
    Then I can see product detail page

    Examples:
        | productName | 
        | ponds men | 

@share_product
Scenario Outline: Verify user able to share the product
    Given I open the browser
    When I type product name "<productName>" and click enter
    When I click card product
    Then I can click share button

    Examples:
        | productName | 
        | ponds men | 