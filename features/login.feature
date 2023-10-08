@login_steps_feature @run
Feature: Login Functionality

@login_on_web_app
Scenario: Login steps
    Given I open the browser 
    When I fill my "username/correct_username" with "field_username/text_field_uname"
    When I fill my "psswd/correct_password" with "field_password/text_field_password"
    When User click "login/btn_login"
    When User wait 3 seconds
    Then Make sure text "title/header_title" with element "title/product_title" is displayed

@login_with_locked_user
Scenario: Login with locked user
    Given I open the browser
    When I fill my "username_block/block_user" with "field_username/text_field_uname"
    When I fill my "psswd/correct_password" with "field_password/text_field_password"
    When User click "login/btn_login"
    When User wait 5 seconds
    Then Make sure text "error_message/block_user_error" with element "element_error/error_locked_user" is displayed