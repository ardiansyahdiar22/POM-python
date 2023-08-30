Feature: Search product

Scenario Outline: Verify user able to search product
    Given I open the browser with "<url>"
    When I type product name "<productName>" and click enter
    When I click card product
    Then I can see product detail page

    Examples:
        | productName | url |
        | ponds men | https://www.tokopedia.com/unilever |