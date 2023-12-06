
*** Settings ***
Documentation           Keywords collections for all test cases
Library                 Folk.py

*** Keywords ***
setup payload data
    [Arguments]         ${test_data}        ${key}
    &{payload}         prepare payload
    ...                 test_data/${test_data}/${test_data}_data.json
    ...                 ${key}
    [Return]            ${payload}