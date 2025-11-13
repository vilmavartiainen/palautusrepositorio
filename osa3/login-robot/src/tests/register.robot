*** Settings ***
Resource  resource.robot
Test Setup  Create User And Input New Command

*** Test Cases ***

Register With Valid Username And Password
    Input Credentials    maija   ljkv823r9y8fer
    Output Should Contain    New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  kalle  ue7re78fbhv
    Output Should Contain   User with username kalle already exists

Register With Too Short Username And Valid Password
    Input Credentials    kai   asdfgh56chj
    Output Should Contain    Username must be longer than 3 characters

Register With Enough Long But Invalid Username And Valid Password
    Input Credentials    nallepuh1   asdfgh56chj
    Output Should Contain    Username should only contain letters

Register With Valid Username And Too Short Password
    Input Credentials    nallepuh  asd123
    Output Should Contain    Password must be longer than 8 character

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials    nallepuh  asdfghjklö
    Output Should Contain    Password must contain both letters and numbers

*** Keywords ***
Create User And Input New Command
    Input New Command
    Create User  kalle  kalle123
    