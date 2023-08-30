Feature: Login Functionality

Scenario Outline: Successful login
    Given I open the browser with "<url>"
    When I enter my "<username>" and "<password>"
    And I click the login button
    Then I should be redirected to the dashboard

    Examples:
        | username | password            | url |
        | standard_user  | secret_sauce  | https://www.saucedemo.com/ |