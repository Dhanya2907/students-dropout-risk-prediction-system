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
## **6.6 IDENTIFY SYSTEM OUTPUTS:**
### **6.6.1 DROPOUT RISK PREDICTION:**
- Low Risk
- Medium Risk
- High Risk
### **6.6.2 ADDITIONAL OUTPUT:**
- Prediction probability/score
- Risk level
- Key factors affecting dropout risk
- Recommended actions
Example:

```text
Prediction: Low Dropout Risk

Risk Level: Low

Recommendation:
Maintain regular attendance and
continue the current academic pattern.
```
Another example:

```text
Prediction: High Dropout Risk

Risk Level: High

Recommendation:
Student requires academic mentoring,
attendance monitoring and additional support.
```
## **7. SYSTEM DESIGN**
### **7.1 INPUTS**
- Student ID
- Student Name
- Attendance %
- Study Hours
- Internal Marks
- Assignment Completion %
- Previous Academic Performance
- Number of Backlogs
## **7.2 PROCESSING**

```text
Validate Input
      ↓
Preprocess Data
      ↓
Feature Selection
      ↓
Send Data to ML Model
      ↓
Generate Prediction
      ↓
Determine Risk Level
      ↓
Generate Recommendation
```
## **7.3 OUTPUTS**
- Predicted dropout risk
- Risk category
- Prediction probability
- Key risk factors
- Recommendation
## **8. SYSTEM ARCHITECTURE**

```text
              Student
                 ↓
        Enter Student Details
                 ↓
        ┌─────────────────┐
        │   Tkinter UI    │
        └─────────────────┘
                 ↓
        Input Validation
                 ↓
        Data Preprocessing
                 ↓
        ┌─────────────────┐
        │  ML Model (.pkl)│
        └─────────────────┘
                 ↓
        Dropout Prediction
                 ↓
        Risk Classification
                 ↓
       AI Recommendation Logic
                 ↓
        ┌─────────────────┐
        │   Result Screen │
        └─────────────────┘
                 ↓
       Risk + Recommendation
```
## **9. UI DESIGN REQUIREMENTS**
The application should contain:
## **9.1 STUDENT INFORMATION SECTION**
- Student ID
- Student Name
## **9.2 ACADEMIC INFORMATION SECTION**
- Attendance
- Study Hours
- Internal Marks
- Assignment Completion
- Previous Performance
- Number of Backlogs
## **9.3 ACTION SECTION**
- Predict Dropout Risk
- Clear
- Exit
## **9.4 RESULT SECTION**
- Predicted Dropout Risk
- Risk Level
- Prediction Probability
- Key Risk Factors
- Recommendation
## **10. IMPLEMENTATION (MACHINE LEARNING MODEL DEVELOPMENT)**
### **10.1 OBJECTIVES**
- Understand the fundamentals of Machine Learning (ML).
- Understand the difference between traditional rule-based systems and ML-based systems.
- Work with datasets using Pandas & NumPy.
- Perform data preprocessing and feature selection.
- Train a Machine Learning model for dropout risk prediction.
- Evaluate model performance using basic metrics.
- Replace rule-based dropout risk logic with an ML-based prediction system.
- Prepare the ML model for integration with Tkinter UI.
- Save the trained model for future predictions.
### **10.2 OUTCOMES**
Should complete:
- Dataset (CSV file)
- Data preprocessing code
- Feature selection
- Trained ML model
- Accuracy report
- Confusion matrix
- Prediction function
- Saved model file (.pkl)
- Tkinter integration
## **10.3 ML WORKFLOW**

```text
Data Collection
      ↓
Data Preprocessing
      ↓
Feature Selection
      ↓
Train-Test Split
      ↓
Model Training
      ↓
Model Evaluation
      ↓
Prediction
      ↓
Save Model (.pkl)
      ↓
Integrate with Tkinter
```
## **10.4 PROBLEM TYPE**
For this Project:
Classification Problem
Output categories:
- Low Risk
- Medium Risk
- High Risk
The classification model predicts which dropout-risk category a student belongs to.
Optional Regression Problem
Output = Dropout Risk Score (0–100)
For example:

```text
0–30   → Low Risk
31–60  → Medium Risk
61–100 → High Risk
```
## **10.5 MODEL SELECTION**
###  **Algorithms Introduced**
###  **Logistic Regression — Primary** 
Used as the main beginner-friendly classification algorithm.
### **Decision Tree — Optional**
Can be used to understand which student factors contribute to the prediction.
### **Random Forest — Advanced**
Can be used to improve prediction performance by combining multiple decision trees.
### **Recommended approach:**

```text
Logistic Regression
       ↓
Evaluate
       ↓
Decision Tree
       ↓
Compare Results
       ↓
Random Forest (Optional)
```
## **10.6 MODEL EVALUATION**
The trained model can be evaluated using:
- Accuracy
- Precision
- Recall
- F1-Score
- Confusion Matrix
## **Confusion Matrix**
The confusion matrix helps identify how correctly the model predicts:

```text
                 Predicted
              Low  Medium  High

Actual Low     ✓      ✗      ✗

Actual Medium  ✗      ✓      ✗

Actual High    ✗      ✗      ✓
```
## **10.7 IMPROVING THE MODEL**
The model can be improved by:
- Increasing dataset size
- Collecting better-quality student data
- Handling missing values
- Feature selection
- Removing irrelevant features
- Balancing the classes
- Trying different algorithms
- Tuning model parameters
- Comparing multiple ML models
- Using cross-validation
- Monitoring model performance
## **Final Project Flow**
Your complete project will finally become:

```text
                    STUDENT
                       ↓
              Enter Student Data
                       ↓
                 Validate Data
                       ↓
               Preprocess Data
                       ↓
                ML MODEL (.pkl)
                       ↓
              Dropout Prediction
                       ↓
        ┌──────────────┼──────────────┐
        ↓              ↓              ↓
     LOW RISK      MEDIUM RISK     HIGH RISK
        ↓              ↓              ↓
     Normal        Monitoring      Intervention
        └──────────────┼──────────────┘
                       ↓
             AI Recommendation
                       ↓
                 Tkinter UI
                       ↓
              Display Final Result
```
