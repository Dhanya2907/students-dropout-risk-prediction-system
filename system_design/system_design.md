# System Design
## Student Dropout Risk Prediction System

## 1. Introduction

The Student Dropout Risk Prediction System is designed to identify students
who may be at risk of dropping out based on their academic performance and
learning-related factors.

The system uses a trained Random Forest Machine Learning model to classify
students into Low, Medium, or High dropout risk categories.

The application is developed using Python and Tkinter for the graphical user
interface. Student information is stored in an Excel file and prediction
results can be sent to an n8n workflow through a webhook.

---

## 2. System Objective

The main objectives of the system are:

- To collect student academic information.
- To validate student input data.
- To store student information securely.
- To predict student dropout risk using Machine Learning.
- To classify students into Low, Medium, and High risk categories.
- To calculate an academic performance score.
- To provide personalized recommendations.
- To display risk statistics through a dashboard.
- To integrate the prediction system with n8n automation.

---

## 3. System Architecture

The system consists of the following major components:

1. User Interface
2. Student Data Management
3. Excel Database
4. Machine Learning Model
5. Risk Prediction Module
6. Performance Score Module
7. Recommendation Module
8. n8n Integration
9. Dashboard

---

## 4. Input Design

The system accepts the following student information:

| Input | Range / Type |
|---|---|
| Student ID | Numeric |
| Student Name | Alphabetic |
| Attendance | 0–100 % |
| Study Hours | 0–10 hours/day |
| Internal Marks | 0–100 |
| Assignment Marks | 0–100 |
| Previous Semester GPA | 0–10 |
| Backlogs | 0 or greater |

---

## 5. Processing Design

The system processes student data using the following sequence:

1. User enters student details.
2. Input validation is performed.
3. Valid student data is stored in Excel.
4. Saved students are loaded for prediction.
5. The Random Forest model receives the required features.
6. The model predicts dropout risk.
7. The system calculates the performance score.
8. The system generates recommendations.
9. Prediction information is displayed to the user.
10. Prediction data is sent to n8n.

---

## 6. Machine Learning Design

The system uses a trained Random Forest classification model.

### Features Used

- Attendance
- Study Hours
- Internal Marks
- Assignment Marks
- Previous Semester GPA
- Number of Backlogs

### Output

The model produces one of the following risk categories:

- LOW
- MEDIUM
- HIGH

The model may also provide prediction probabilities when supported by
the trained model.

---

## 7. Performance Score Design

The system calculates an additional performance score using normalized
student academic information.

### Study Hours Score

Study hours are normalized using:

Study Hours Score = min((Study Hours / 10) × 100, 100)

### GPA Score

GPA is normalized using:

GPA Score = min((GPA / 10) × 100, 100)

### Backlog Score

Backlog score is calculated using:

Backlog Score = max(0, 100 - (Backlogs × 20))

### Final Performance Score

The final score is calculated using:

Score =
(Attendance × 0.20)
+
(Study Hours Score × 0.15)
+
(Internal Marks × 0.20)
+
(Assignment Marks × 0.15)
+
(GPA Score × 0.20)
+
(Backlog Score × 0.10)

The final score is displayed on a 0–100 scale.

---

## 8. Recommendation Design

The recommendation module analyzes student performance.

### Attendance

If attendance is low, the system recommends improving class attendance.

### Study Hours

If study hours are low, the system recommends increasing daily study time.

### Internal Marks

If internal marks are low, the system recommends regular revision and
practice.

### Assignment Marks

If assignment marks are low, the system recommends completing assignments
regularly and improving submission quality.

### GPA

If GPA is low, the system recommends focusing on weak subjects and
improving academic preparation.

### Backlogs

If backlogs exist, the system recommends clearing pending subjects.

---

## 9. Dashboard Design

The dashboard displays:

- Total Students
- High Risk Students
- Medium Risk Students
- Low Risk Students

The risk cards can be selected to display students belonging to each
risk category.

---

## 10. Data Storage Design

Student information is stored in:

student_details.xlsx

The Excel file contains:

- Student ID
- Student Name
- Attendance
- Study Hours
- Internal Marks
- Assignment Marks
- Previous Semester GPA
- Backlogs

The system supports:

- Adding new students
- Updating existing students
- Viewing student records
- Sorting students by Student ID

---

## 11. n8n Integration Design

The application communicates with n8n using an HTTP POST webhook.

The following information is sent:

- Student ID
- Student Name
- Attendance
- Study Hours
- Internal Marks
- Assignment Marks
- Previous Semester GPA
- Backlogs
- Prediction
- Risk
- Performance Score
- Recommendations
- Prediction Probability

The n8n workflow can then be used for further automation such as
notifications, emails, logging, or AI-based analysis.

---

## 12. Output Design

The system displays:

- Student Name
- Student ID
- ML Prediction
- Dropout Risk
- Performance Score
- Prediction Probability
- Student Performance Details
- Personalized Recommendations
- n8n Integration Status

---

## 13. Overall System Flow

User
  ↓
Student Details
  ↓
Input Validation
  ↓
Excel Storage
  ↓
Select Saved Student
  ↓
Machine Learning Model
  ↓
Dropout Risk Prediction
  ↓
Performance Score
  ↓
Recommendations
  ↓
Dashboard / Prediction Result
  ↓
n8n Webhook
  ↓
Automation

---

## 14. Technology Stack

### Frontend
- Python Tkinter

### Programming Language
- Python

### Machine Learning
- Scikit-learn
- Random Forest Classifier

### Model Storage
- Joblib

### Database / Storage
- Microsoft Excel
- OpenPyXL

### Automation
- n8n Webhook

### HTTP Communication
- Requests Library

---

## 15. System Design Conclusion

The system is designed as a modular student dropout risk prediction
application. The design separates user interaction, data storage,
machine learning prediction, performance analysis, recommendation
generation, and automation.

This design provides a clear foundation for the subsequent Architecture
Design, Module Design, Implementation, and Testing phases of the V-Model.