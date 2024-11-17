*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application Create User And Go To Register Page

*** Test Cases ***

Register With Valid Username And Password
    Set Username  validiuseri
    Set Password  validisalasana1234
    Set Password Confirmation  validisalasana1234
    Submit Credentials
    Register Should Succeed 

Register With Too Short Username And Valid Password
    Set Username  öö
    Set Password  validisalasana1234
    Set Password Confirmation  validisalasana1234
    Submit Credentials
    Register Should Fail With Message  Too short username

Register With Valid Username And Too Short Password
    Set Username  validiuseri
    Set Password  12
    Set Password Confirmation  12
    Submit Credentials
    Register Should Fail With Message  Password should be over 8 chars


Register With Valid Username And Invalid Password
    Set Username  validiuseri
    Set Password  ilmannumeroita
    Set Password Confirmation  ilmannumeroita
    Submit Credentials
    Register Should Fail With Message  Password should consist from more than characters a-z

Register With Nonmatching Password And Password Confirmation
    Set Username  validiuseri
    Set Password  validisalasana1234
    Set Password Confirmation  erisalasana1234
    Submit Credentials
    Register Should Fail With Message  Passwords dont match

Register With Username That Is Already In Use
    Set Username  validiuseri
    Set Password  validisalasana1234
    Set Password Confirmation  validisalasana1234
    Submit Credentials
    Go To Register Page
    Set Username  validiuseri
    Set Password  erisalasana1234
    Set Password Confirmation  erisalasana1234
    Submit Credentials
    Register Should Fail With Message  Username already in use

Login After Succesful Registeration
    Set Username  validiuseri
    Set Password  validisalasana1234
    Set Password Confirmation  validisalasana1234
    Submit Credentials
    Register Should Succeed
    Go To Main Page
    Click Button  Logout
    Set Username  validiuseri
    Set Password  validisalasana1234
    Click Button  Login
    Login Should Succeed
    

Login After Failed Registeration
    Set Username  validiuseri
    Set Password  huonosalasana
    Set Password Confirmation  huonosalasana
    Submit Credentials
    Register Should Fail With Message  Password should consist from more than characters a-z
    Go To Main Page
    Click Button  Logout
    Set Username  validiuseri
    Set Password  huonosalasana
    Click Button  Login
    Login Should Fail With Message  Invalid username or password

*** Keywords ***
Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Text  password  ${password}

Set Password Confirmation
    [Arguments]  ${password_confirmation}
    Input Text  password_confirmation  ${password_confirmation}

Register Should Succeed
    Welcome Page Should Be Open

Submit Credentials
    Click Button  Register

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Login Should Succeed
    Main Page Should Be Open

Login Should Fail With Message
    [Arguments]  ${message}
    Login Page Should Be Open
    Page Should Contain  ${message}

Reset Application Create User And Go To Register Page
    Reset Application
    Create User  kalle  kalle123
    Go To Register Page