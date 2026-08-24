import os
import unittest
import openpyxl
import joblib


FILE_NAME = "student_details.xlsx"
MODEL_FILE = "dropout_risk_model.pkl"


def check_student_details():
    return os.path.exists(FILE_NAME)


def check_prediction_model():
    return os.path.exists(MODEL_FILE)


def load_students():
    if not os.path.exists(FILE_NAME):
        return []

    workbook = openpyxl.load_workbook(
        FILE_NAME,
        data_only=True
    )

    sheet = workbook.active
    students = []

    for row in sheet.iter_rows(
        min_row=2,
        values_only=True
    ):
        if not row[0]:
            continue

        try:
            students.append({
                "id": str(row[0]),
                "name": str(row[1]),
                "attendance": float(row[2]),
                "study_hours": float(row[3]),
                "internal": float(row[4]),
                "assignment": float(row[5]),
                "gpa": float(row[6]),
                "backlogs": int(row[7])
            })

        except (
            ValueError,
            TypeError,
            IndexError
        ):
            continue

    workbook.close()

    return students


def load_model():
    if not os.path.exists(MODEL_FILE):
        return None

    try:
        return joblib.load(MODEL_FILE)

    except Exception:
        return None


def predict_dropout_risk(student):

    model = load_model()

    if model is None:
        return None

    features = [[
        student["attendance"],
        student["study_hours"],
        student["internal"],
        student["assignment"],
        student["gpa"],
        student["backlogs"]
    ]]

    prediction = model.predict(
        features
    )[0]

    return str(prediction).upper()


def calculate_score(student):

    study_score = min(
        (student["study_hours"] / 10) * 100,
        100
    )

    gpa_score = min(
        (student["gpa"] / 10) * 100,
        100
    )

    backlog_score = max(
        0,
        100 - (student["backlogs"] * 20)
    )

    score = (
        student["attendance"] * 0.20
        + study_score * 0.15
        + student["internal"] * 0.20
        + student["assignment"] * 0.15
        + gpa_score * 0.20
        + backlog_score * 0.10
    )

    return round(score, 2)


def generate_recommendations(student):

    recommendations = []

    if student["attendance"] < 75:
        recommendations.append(
            "Improve attendance."
        )

    if student["study_hours"] < 4:
        recommendations.append(
            "Increase daily study hours."
        )

    if student["internal"] < 50:
        recommendations.append(
            "Improve internal marks."
        )

    if student["assignment"] < 50:
        recommendations.append(
            "Complete assignments regularly."
        )

    if student["gpa"] < 6:
        recommendations.append(
            "Focus on improving GPA."
        )

    if student["backlogs"] > 0:
        recommendations.append(
            "Clear pending backlogs."
        )

    if not recommendations:
        recommendations.append(
            "Continue maintaining good academic performance."
        )

    return recommendations


class TestAcceptanceCriteria(unittest.TestCase):

    def test_student_details_available(self):

        self.assertTrue(
            check_student_details()
        )


    def test_prediction_model_available(self):

        self.assertTrue(
            check_prediction_model()
        )


    def test_student_information_available(self):

        students = load_students()

        self.assertGreater(
            len(students),
            0
        )


    def test_dropout_prediction_requirement(self):

        students = load_students()

        student = students[0]

        prediction = predict_dropout_risk(
            student
        )

        self.assertIn(
            prediction,
            [
                "LOW",
                "MEDIUM",
                "HIGH"
            ]
        )


    def test_performance_score_requirement(self):

        students = load_students()

        student = students[0]

        score = calculate_score(
            student
        )

        self.assertGreaterEqual(
            score,
            0
        )

        self.assertLessEqual(
            score,
            100
        )


    def test_recommendation_requirement(self):

        students = load_students()

        student = students[0]

        recommendations = generate_recommendations(
            student
        )

        self.assertIsInstance(
            recommendations,
            list
        )

        self.assertGreater(
            len(recommendations),
            0
        )


    def test_complete_user_requirement(self):

        students = load_students()

        self.assertGreater(
            len(students),
            0
        )

        student = students[0]

        prediction = predict_dropout_risk(
            student
        )

        score = calculate_score(
            student
        )

        recommendations = generate_recommendations(
            student
        )

        self.assertIn(
            prediction,
            [
                "LOW",
                "MEDIUM",
                "HIGH"
            ]
        )

        self.assertGreaterEqual(
            score,
            0
        )

        self.assertLessEqual(
            score,
            100
        )

        self.assertGreater(
            len(recommendations),
            0
        )


if __name__ == "__main__":
    unittest.main(
        verbosity=2
    )