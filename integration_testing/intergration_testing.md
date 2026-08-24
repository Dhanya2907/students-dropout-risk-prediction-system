# Integration Testing

## Objective

Integration testing verifies whether the major modules
of the Student Dropout Risk Prediction System work together
correctly.

## Modules Integrated

- Student Details Module
- Excel Database
- Machine Learning Model
- Risk Prediction Module
- Recommendation Module

## Integration Flow

Student Details
→ Excel Database
→ Student Data Loading
→ Machine Learning Model
→ Dropout Risk Prediction
→ Recommendation Generation

## Test Cases

| Test Case | Integration | Expected Result |
|-----------|-------------|-----------------|
| Save and Load Student | Excel + Student Module | Student data loaded successfully |
| Load ML Model | Model File + Prediction Module | Model loads successfully |
| Student Prediction | Excel + ML Model | LOW/MEDIUM/HIGH prediction generated |
| Prediction + Recommendation | ML + Recommendation | Risk and recommendations generated |

## Result

The integration tests verify that the Student Details,
Excel database, Machine Learning model, prediction module,
and recommendation module communicate correctly.

The integrated system should successfully process student
data and generate the corresponding dropout risk prediction
and recommendations.