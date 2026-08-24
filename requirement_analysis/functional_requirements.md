# Functional Requirements
## Student Dropout Risk Prediction System

### 1. Student Registration
- The system shall allow users to enter Student ID.
- The system shall allow users to enter Student Name.
- The system shall collect Attendance Percentage.
- The system shall collect Study Hours per Day.
- The system shall collect Internal Marks.
- The system shall collect Assignment Marks.
- The system shall collect Previous Semester GPA.
- The system shall collect Number of Backlogs.

### 2. Input Validation
- Student ID shall accept numeric values.
- Student Name shall accept alphabets and spaces.
- Attendance shall be between 0 and 100.
- Study Hours shall be between 0 and 10.
- Internal Marks shall be between 0 and 100.
- Assignment Marks shall be between 0 and 100.
- GPA shall be between 0 and 10.
- Backlogs shall not accept negative values.

### 3. Student Data Management
- The system shall save student details in an Excel file.
- The system shall allow existing student information to be updated.
- The system shall prevent invalid student records from being saved.
- The system shall display saved student records.

### 4. Machine Learning Prediction
- The system shall load the trained Random Forest model.
- The system shall use student academic information as input.
- The system shall predict dropout risk.
- The prediction shall classify students as LOW, MEDIUM, or HIGH risk.
- The system shall display prediction probability when available.

### 5. Performance Score
- The system shall calculate an academic performance score.
- The score shall be calculated using attendance, study hours, internal marks, assignment marks, GPA, and backlogs.
- The score shall be displayed on a 0–100 scale.

### 6. Risk Dashboard
- The system shall display total number of students.
- The system shall display the number of high-risk students.
- The system shall display the number of medium-risk students.
- The system shall display the number of low-risk students.
- Users shall be able to view students based on risk category.

### 7. Recommendations
- The system shall analyze student academic performance.
- The system shall identify areas requiring improvement.
- The system shall provide personalized recommendations.
- Recommendations shall consider attendance, study hours, internal marks, assignment marks, GPA, and backlogs.

### 8. Student List
- The system shall display all saved students.
- Student records shall display Student ID, Name, Attendance, Study Hours, Internal Marks, Assignment Marks, GPA, and Backlogs.
- Student records shall be sorted by Student ID.

### 9. n8n Integration
- The system shall send prediction data to the configured n8n webhook.
- The system shall send Student ID and Student Name.
- The system shall send academic details.
- The system shall send predicted risk.
- The system shall send performance score.
- The system shall send recommendations.
- The system shall display whether the n8n workflow was successfully triggered.

### 10. Application Control
- The system shall provide Dashboard navigation.
- The system shall provide Student Details navigation.
- The system shall provide Student List navigation.
- The system shall provide Risk Prediction navigation.
- The system shall provide Clear functionality.
- The system shall provide Exit functionality.