*** Settings ***
Documentation         Test collection for registration system
Resource              ../resources/common.resource


*** Test Cases ***
Register with valid credentials
    [Documentation]     verifies that user can register into the system with valid credentials
    [Tags]              smoke
    ${payload}          setup payload data
    ...                 test_data=user
    ...                 key=user_1
    post request        url=https://study-hub-backend.onrender.com
    ...                 payload= ${payload}
