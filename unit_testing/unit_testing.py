import unittest


def validate_attendance(attendance):
    return 0 <= attendance <= 100


def validate_study_hours(hours):
    return 0 <= hours <= 10


def validate_gpa(gpa):
    return 0 <= gpa <= 10


def validate_backlogs(backlogs):
    return backlogs >= 0


def calculate_performance_score(
    attendance,
    study_hours,
    internal,
    assignment,
    gpa,
    backlogs
):
    study_score = min(
        (study_hours / 10) * 100,
        100
    )

    gpa_score = min(
        (gpa / 10) * 100,
        100
    )

    backlog_score = max(
        0,
        100 - (backlogs * 20)
    )

    score = (
        attendance * 0.20
        + study_score * 0.15
        + internal * 0.20
        + assignment * 0.15
        + gpa_score * 0.20
        + backlog_score * 0.10
    )

    return round(score, 2)


class TestStudentValidation(unittest.TestCase):

    def test_valid_attendance(self):
        self.assertTrue(
            validate_attendance(85)
        )

    def test_invalid_attendance(self):
        self.assertFalse(
            validate_attendance(105)
        )

    def test_valid_study_hours(self):
        self.assertTrue(
            validate_study_hours(6)
        )

    def test_invalid_study_hours(self):
        self.assertFalse(
            validate_study_hours(12)
        )

    def test_valid_gpa(self):
        self.assertTrue(
            validate_gpa(8.5)
        )

    def test_invalid_gpa(self):
        self.assertFalse(
            validate_gpa(11)
        )

    def test_valid_backlogs(self):
        self.assertTrue(
            validate_backlogs(2)
        )

    def test_invalid_backlogs(self):
        self.assertFalse(
            validate_backlogs(-1)
        )


class TestPerformanceScore(unittest.TestCase):

    def test_score_range(self):

        score = calculate_performance_score(
            90,
            8,
            85,
            90,
            8.5,
            0
        )

        self.assertGreaterEqual(
            score,
            0
        )

        self.assertLessEqual(
            score,
            100
        )


if __name__ == "__main__":
    unittest.main(
        verbosity=2
    )