# students-dropout-risk-prediction-system
## **1. PROBLEM STATEMENT:**
- Student dropout can be influenced by multiple academic, behavioral, attendance, and personal factors.
- Faculty and academic coordinators may find it difficult to identify students who are at risk of dropping out at an early stage.
- A data-driven system can help predict the dropout risk of students based on historical and current student information.
- The system can provide early warnings and recommendations to help improve student retention.
## **2. PROPOSED SOLUTION:**
- Collect student-related information.
- Process and validate the entered data.
- Use a Machine Learning model to predict dropout risk.
- Classify students based on their predicted dropout risk.
- Identify factors that may contribute to dropout risk.
- Generate intelligent recommendations.
- Display the results through a user-friendly Tkinter interface.
## **3. PROCESS FLOW:**


```text
Start
  ↓
Enter Student Details
  ↓
Validate Input
  ↓
Preprocess Data
  ↓
ML Prediction
  ↓
Determine Dropout Risk Level
  ↓
Generate AI Recommendation
  ↓
Display Result
  ↓
End
```
## **4. PROJECT MAPPING:**

| V-Model Stage             | Student Dropout Risk Project                 |
| ------------------------- | -------------------------------------------- |
| Requirement Analysis      | Identify student dropout risk problem        |
| System Design             | Design system architecture and UI            |
| Implementation            | Develop Python + ML application              |
| Integration               | Integrate UI, ML and AI recommendation logic |
| Testing                   | Test individual modules and complete system  |
| Validation                | Check system against requirements            |
| Demonstration             | Present working capstone                     |

## **5. PROJECT - MODULAR APPLICATION DEVELOPMENT:**
### **Create separate functions:**

```text
get_student_data()
validate_input()
preprocess_data()
predict_dropout_risk()
generate_recommendation()
display_result()
```
These functions help divide the application into smaller and easily testable modules.
## **6. REQUIREMENT ANALYSIS:**
### **6.1 FUNCTIONAL REQUIREMENTS:**
The system should:
- Accept student details.
- Validate user inputs.
- Store/process student information.
- Preprocess input data.
- Apply the trained ML model.
- Predict student dropout risk.
- Classify the student into a risk category.
- Generate recommendations.
- Display results through the GUI.
- Handle invalid inputs.
- Provide a reset/clear option.
### **6.2 NON-FUNCTIONAL REQUIREMENTS:**
The application should be:
- User-friendly
- Easy to understand
- Fast in generating predictions
- Reliable
- Maintainable
- Scalable
- Secure with respect to student data
- Easy to test
### **6.3 IDENTIFY THE USER:**
Primary users may include:
- Faculty
- Academic coordinators
- Mentors
- Students
- Student support teams
## **6.4 USER REQUIREMENT:**
The user should be able to:
- Enter student information.
- Submit the information for analysis.
- View predicted dropout risk.
- Understand the student's risk level.
- Identify important risk factors.
- Receive recommendations for improvement.
## **6.5 IDENTIFY SYSTEM INPUTS:**
The initial system can use:
- Student ID
- Student Name
- Attendance Percentage
- Study Hours per Day
- Internal Assessment Marks
- Assignment Completion Percentage
- Previous Academic Performance
- Number of Backlogs
