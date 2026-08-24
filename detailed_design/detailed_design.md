# Detailed Design

## Objective

Detailed design describes the internal functions and processing
logic of each system module.

## Student Data Module

### Input

- Student ID
- Student Name
- Attendance
- Study Hours
- Internal Marks
- Assignment Marks
- GPA
- Backlogs

### Processing

- Validate fields
- Validate numeric ranges
- Check duplicate Student ID
- Store student information

### Output

Validated student record.

## Machine Learning Module

### Input

Six academic features:

1. Attendance
2. Study Hours
3. Internal Marks
4. Assignment Marks
5. Previous Semester GPA
6. Backlogs

### Processing

The trained Random Forest model is loaded and used for prediction.

### Output

- LOW
- MEDIUM
- HIGH

## Performance Score Module

The system calculates a performance score using weighted academic
parameters.

The score is represented between 0 and 100.

## Recommendation Module

The system checks weak areas such as:

- Attendance
- Study Hours
- Internal Marks
- Assignment Marks
- GPA
- Backlogs

Based on the identified areas, personalized recommendations are
generated.

## Automation Module

Prediction details are sent to the n8n webhook.

The workflow can be used for:

- Notifications
- Email automation
- Reporting
- Further AI processing

## Conclusion

Detailed design defines the internal processing logic required for
implementation.