@login_steps_feature @run
Feature: Login Functionality

@login_on_web_app
Scenario Outline: Login steps
    Given I open the browser 
    When User click button login
    When I enter my "<email>"
    Then Button login is enabled

    Examples:
        | email |  
        | diar@gmail.com  |  