@login_steps_feature @run
Feature: Login Functionality

@login_btn_next_enable
Scenario: Verify button next enable
    Given I open the browser 
    When User click "button_login/login_btn_example"
    When I fill my "emailUser/input_email" with "email_form/form_input_email"
    When User wait 5 seconds
    Then "button_login/button_next" is enabled

@login_on_web_app
Scenario: Login steps
    Given I open the browser 
    When I fill my "username/correct_username" with "field_username/text_field_uname"
    When I fill my "psswd/correct_password" with "field_password/text_field_password"
    When User click "login/btn_login"
    When User wait 3 seconds
    Then Make sure text "title/header_title" with element "title/product_title" is displayed