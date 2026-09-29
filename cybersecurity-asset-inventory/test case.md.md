# Sheet1
Test Case ID | Module | Test Scenario | Test Input | Expected Result | Result
TC01 | Add Asset | Enter valid asset details | Asset A104 with valid type/risk/status | Asset added successfully | Pass
TC02 | Add Asset | Use an existing Asset ID | A101 | System rejects duplicate ID | Pass
TC03 | Search Asset | Search using Asset ID | A101 | A101 asset details are displayed | Pass
TC04 | Search Asset | Search using asset name | Web-Server | Matching asset is displayed | Pass
TC05 | Update Asset | Update an existing asset | A101 → change department/status | Updated details are saved | Pass
TC06 | Delete Asset | Delete an existing asset | A103 | Asset is removed from inventory | Pass
TC07 | Display Assets | Display all stored assets | Menu option 5 | All assets and details are displayed | Pass
TC08 | Risk Classification | Check Critical risk count | A102 = Critical | Critical Assets = 1 for sample data | Pass
TC09 | Security Status | Check Vulnerable count | A102 = Vulnerable | Vulnerable Assets = 1 for sample data | Pass
TC10 | Invalid Menu Input | Enter an invalid menu choice | 9 | System displays invalid choice message | Pass