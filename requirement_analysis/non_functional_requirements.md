# Non-Functional Requirements
## Student Dropout Risk Prediction System

### 1. Performance
- The system should generate predictions quickly.
- Student records should load without unnecessary delay.
- The dashboard should display risk statistics efficiently.

### 2. Usability
- The graphical user interface should be simple and user-friendly.
- Navigation should be clear.
- Input fields should have meaningful labels.
- Error messages should be understandable.

### 3. Reliability
- The system should handle invalid input safely.
- The system should handle missing model files gracefully.
- The system should handle Excel file errors.
- The system should handle n8n connection failures without crashing.

### 4. Accuracy
- The system should use the trained machine learning model for prediction.
- The prediction should be based on the required student academic features.
- The system should provide consistent results for the same input data.

### 5. Maintainability
- The application should use modular functions.
- Machine learning, data storage, prediction, recommendation, and UI operations should be separated logically.
- The source code should be readable and easy to modify.

### 6. Security
- Student information should be protected from unauthorized access.
- Sensitive configuration information should not be exposed in source code.
- User input should be validated before processing.

### 7. Scalability
- The system should support storing multiple student records.
- The system should allow additional student features to be added in the future.
- The machine learning model should be replaceable without redesigning the complete interface.

### 8. Compatibility
- The system should run on a system supporting Python and Tkinter.
- The system should support the required Python libraries.
- The system should work with the trained Random Forest model.

### 9. Availability
- The application should be available whenever the required Python environment and model are present.
- The system should continue providing local predictions even if the n8n service is temporarily unavailable.

### 10. Extensibility
- Additional machine learning models can be integrated in the future.
- Additional testing modules can be added.
- Additional notification services such as email can be integrated.