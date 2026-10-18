import unittest


def check_pass_status(score: int) -> str:
    """
    Return whether a student passed, rejecting invalid scores.
    """
    if type(score) is not int:
        raise TypeError("score must be an integer")
    if not 0 <= score <= 100:
        raise ValueError("score must be between 0 and 100")

    if score >= 60:
        return "Pass"
    return "Fail"

class CheckPassStatusTests(unittest.TestCase):
    def test_scores_below_passing_grade_fail(self):
        self.assertEqual(check_pass_status(0), "Fail")
        self.assertEqual(check_pass_status(59), "Fail")

    def test_scores_at_or_above_passing_grade_pass(self):
        self.assertEqual(check_pass_status(60), "Pass")
        self.assertEqual(check_pass_status(100), "Pass")

    def test_scores_outside_valid_range_are_rejected(self):
        for score in (-1, 101):
            with self.subTest(score=score):
                with self.assertRaises(ValueError):
                    check_pass_status(score)

    def test_non_integer_scores_are_rejected(self):
        for score in (60.0, "60", True):
            with self.subTest(score=score):
                with self.assertRaises(TypeError):
                    check_pass_status(score)


if __name__ == "__main__":
    print("Example results:")
    for score in (45, 60, 101, 72.5):
        try:
            result = check_pass_status(score)
        except (TypeError, ValueError) as error:
            result = f"Rejected ({error})"
        print(f"Input: {score} -> {result}")

    unittest.main(verbosity=2)