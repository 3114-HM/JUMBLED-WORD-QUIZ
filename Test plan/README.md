
## HIGH LEVEL TEST PLAN


| Test ID | Description | Expected i/p | Expected o/p | Actual o/p | Status |
| ---     | ---         | ---          | ---          | ---        | ---    |
| `HRO1`  |  start the jumbled quiz | click start button | displaying menu list | displaying menu list | pass |
| `HRO2`  | check if the menu displayed or not |select the one button in the menu  | redirect into the selected category |selected category displayed | pass |
| `HRO3`  | if we want to reach again on home page | click on back arrow button | home page | home page | pass |                                       
| `HRO4`  | play the game what you choosed | type the assumed jumbled word | wrong answer | correct answer | fail |
| `HRO5`  | if we want check answer we can select from menu | click on answer button | Answer will be displayed |  answer displayed points decreased by 5| pass |
| `HRO6`  | if we want to change the word | click on change button | the jumble word changed | jumble word changed | pass |


## LOW LEVEL TEST PLAN


| Test ID | Description | Expected i/p | Expected o/p | Actual o/p | Status |
| ---     | ---         | ---          | ---          | ---        | ---    |
| `LO1`   | Enter the correct word from  menu | Enter word | word is correct | correct | pass |
| `LO2`   | Enter the word from menu RONGEA | ORANGE | ORANGE | ORANGE points : 5 | pass | 
| `LO3`   | Enter the word from menu RONGEA | ERANGO | RENAOG  | ORANGE | fail |
| `LO4`   | If we want check answer we can select from menu | Answer will be displayed | Answer will be displayed | No Points answer displayed | pass |
| `LO5`  |we can select what feature we want from menu | Type valid word | correct points : 6 | correct points : 5 | fail |
| `LO6`  |Enter the word from menu rtactro |TrAcTor|tractor|tractor points:5|pass|




