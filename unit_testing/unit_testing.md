# Unit Testing

## Objective

Unit testing verifies individual functions and components
of the Student Dropout Risk Prediction System.

## Components Tested

- Attendance validation
- Study hours validation
- GPA validation
- Backlog validation
- Performance score calculation

## Test Cases

| Test Case | Input | Expected Result |
|-----------|-------|-----------------|
| Valid Attendance | 85 | Pass |
| Invalid Attendance | 105 | Fail |
| Valid Study Hours | 6 | Pass |
| Invalid Study Hours | 12 | Fail |
| Valid GPA | 8.5 | Pass |
| Invalid GPA | 11 | Fail |
| Valid Backlogs | 2 | Pass |
| Invalid Backlogs | -1 | Fail |
| Performance Score | Valid student data | 0–100 |

## Result

All individual functions are tested independently.