import joblib
import os

MODEL_FILE = "dropout_risk_model.pkl"


def load_model():
    if not os.path.exists(MODEL_FILE):
        raise FileNotFoundError(
            f"Model file not found: {MODEL_FILE}"
        )

    return joblib.load(MODEL_FILE)


def predict_dropout_risk(
    attendance,
    study_hours,
    internal_marks,
    assignment_marks,
    previous_semester_gpa,
    backlogs
):
    model = load_model()

    input_data = [[
        float(attendance),
        float(study_hours),
        float(internal_marks),
        float(assignment_marks),
        float(previous_semester_gpa),
        int(backlogs)
    ]]

    prediction = model.predict(input_data)[0]
    prediction = str(prediction).upper().strip()

    if prediction in ["LOW", "0"]:
        risk_level = "LOW"
        risk_score = 25

    elif prediction in ["MEDIUM", "MEDIUM RISK", "1"]:
        risk_level = "MEDIUM"
        risk_score = 60

    elif prediction in ["HIGH", "HIGH RISK", "2"]:
        risk_level = "HIGH"
        risk_score = 85

    else:
        risk_level = prediction
        risk_score = 50

    improvement_areas = []

    if float(attendance) < 75:
        improvement_areas.append("Attendance")

    if float(study_hours) < 3:
        improvement_areas.append("Study Hours")

    if float(internal_marks) < 50:
        improvement_areas.append("Internal Marks")

    if float(assignment_marks) < 50:
        improvement_areas.append("Assignment Marks")

    if float(previous_semester_gpa) < 6:
        improvement_areas.append("Previous Semester GPA")

    if int(backlogs) > 0:
        improvement_areas.append("Backlogs")

    if risk_level == "HIGH":
        recommendation = (
            "Immediate academic support is required. "
            "Improve attendance, study hours and academic performance."
        )

    elif risk_level == "MEDIUM":
        recommendation = (
            "Student requires regular monitoring. "
            "Focus on weak academic areas and improve study habits."
        )

    else:
        recommendation = (
            "Student is currently at low dropout risk. "
            "Continue maintaining good academic performance."
        )

    return {
        "risk_level": risk_level,
        "risk_score": risk_score,
        "recommendation": recommendation,
        "improvement_areas": improvement_areas
    }