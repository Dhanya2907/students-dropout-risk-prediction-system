def get_input():

    attendance = int(input("Enter the attendance percentage: "))
    study_hours = float(input("Enter the number of study hours: "))
    internal_marks = int(input("Enter the internal marks: "))
    assignment_marks = int(input("Enter the assignment marks: "))
    previous_semester_gpa = float(input("Enter the previous semester GPA: "))
    backlogs = int(input("Enter the number of backlogs: "))
    exam_performance = int(input("Enter the exam performance percentage: "))

    return (
        attendance,
        study_hours,
        internal_marks,
        assignment_marks,
        previous_semester_gpa,
        backlogs,
        exam_performance
    )


def normalize_values(study_hours, previous_semester_gpa, backlogs):

    study_hours_score = min((study_hours / 8) * 100, 100)

    gpa_score = min((previous_semester_gpa / 10) * 100, 100)

    backlog_score = max(0, 100 - (backlogs * 20))

    return study_hours_score, gpa_score, backlog_score


def predict_risk(
    attendance,
    study_hours_score,
    internal_marks,
    assignment_marks,
    gpa_score,
    backlog_score,
    exam_performance
):

    risk_score = (
        attendance * 0.20 +
        study_hours_score * 0.10 +
        internal_marks * 0.20 +
        assignment_marks * 0.10 +
        gpa_score * 0.15 +
        backlog_score * 0.10 +
        exam_performance * 0.15
    )

    return round(risk_score, 2)


# Get input
(
    attendance,
    study_hours,
    internal_marks,
    assignment_marks,
    previous_semester_gpa,
    backlogs,
    exam_performance
) = get_input()


# Normalize values
study_hours_score, gpa_score, backlog_score = normalize_values(
    study_hours,
    previous_semester_gpa,
    backlogs
)

result = predict_risk(
    attendance,
    study_hours_score,
    internal_marks,
    assignment_marks,
    gpa_score,
    backlog_score,
    exam_performance
)


print("Risk Score:", result)
if result >= 75:
    risk_level = "LOW RISK"
elif result >= 50:
    risk_level = "MEDIUM RISK"
else:
    risk_level = "HIGH RISK"

print("Risk Score:", result)
print("Risk Level:", risk_level)