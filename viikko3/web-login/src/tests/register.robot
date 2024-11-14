*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application Create User And Go To Register Page

*** Test Cases ***

Register With Valid Username And Password
    Set Username  maija
    Set Password  maija123
    Set Password Confirmation  maija123
    Click Button  Register
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  m
    Set Password  maija123
    Set Password Confirmation  maija123
    Click Button  Register
    Page Should Contain  Username is too short

Register With Valid Username And Too Short Password
    Set Username  maija
    Set Password  m
    Set Password Confirmation  m
    Click Button  Register
    Page Should Contain  Password is too short

Register With Valid Username And Invalid Password
# salasana ei sisällä halutunlaisia merkkejä
    Set Username  maija
    Set Password  maijamaija
    Set Password Confirmation  maijamaija
    Click Button  Register
    Page Should Contain  Password needs to contain alphabets and digits

Register With Nonmatching Password And Password Confirmation
    Set Username  maija
    Set Password  maija123
    Set Password Confirmation  maija122
    Click Button  Register
    Page Should Contain  Passwords do not match

Register With Username That Is Already In Use
    Set Username  kalle
    Set Password  kalle123
    Set Password Confirmation  kalle123
    Click Button  Register
    Page Should Contain  User with username kalle already exists

*** Keywords ***
Reset Application Create User And Go To Register Page
  Reset Application
  Create User  kalle  kalle123
  Go To Register Page

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password_confirmation}
    Input Password  password_confirmation  ${password_confirmation}

Register Should Succeed
    Title Should Be  Welcome to Ohtu Application!