# System Testing

## Objective

System testing verifies the complete Student Dropout Risk
Prediction System as a single integrated application.

## System Components Tested

- Student Details
- Excel Database
- Machine Learning Model
- Risk Prediction
- Performance Score
- Recommendation Generation
- Complete Prediction Flow

## System Flow

User
→ Student Details
→ Save Student
→ Excel Database
→ Select Student
→ Machine Learning Model
→ Dropout Risk Prediction
→ Performance Score
→ Recommendations
→ Result Display

## Test Cases

| Test Case | Input / Action | Expected Result |
|-----------|----------------|-----------------|
| Excel Database | Open application | Database available |
| ML Model | Load model | Model loads successfully |
| Student Data | Select saved student | Student details displayed |
| Risk Prediction | Click Predict | LOW/MEDIUM/HIGH generated |
| Performance Score | Valid student data | Score between 0 and 100 |
| Recommendation | Prediction generated | Recommendations displayed |
| Complete Flow | Student → Prediction | Complete result generated |

## Result

The complete system is tested as a single application.

The system successfully reads student information, loads the
trained Random Forest model, predicts dropout risk, calculates
the performance score, and generates suitable recommendations.

## Conclusion

System testing confirms that the major functions of the
Student Dropout Risk Prediction System work together correctly
and produce the expected output.