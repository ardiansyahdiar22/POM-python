Feature: Example feature implement POM

Scenario Outline: Perform a search function
    Given User Open the browser
    When User login with username "<username>"
    And User click search button
    Then User should be search result for "<username>"

    Examples:
        | username | 
        | testUser |

