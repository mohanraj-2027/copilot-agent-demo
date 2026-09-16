import unittest
from io import StringIO
from unittest.mock import patch

import main


class CalculatorTests(unittest.TestCase):
    def test_add(self):
        self.assertEqual(main.add(2, 3), 5)

    def test_subtract(self):
        self.assertEqual(main.subtract(7, 4), 3)

    def test_multiply(self):
        self.assertEqual(main.multiply(6, 3), 18)

    def test_divide(self):
        self.assertEqual(main.divide(8, 2), 4)

    def test_divide_by_zero_raises_error(self):
        with self.assertRaisesRegex(ValueError, "Cannot divide by zero"):
            main.divide(8, 0)

    def test_is_numeric_accepts_numeric_values(self):
        self.assertTrue(main.is_numeric("12.5"))
        self.assertTrue(main.is_numeric("-3"))

    def test_is_numeric_rejects_nonnumeric_values(self):
        self.assertFalse(main.is_numeric("abc"))
        self.assertFalse(main.is_numeric(""))
        self.assertFalse(main.is_numeric(None))

    @patch("builtins.input", side_effect=["8", "/", "2"])
    def test_main_prints_calculation_result(self, mocked_input):
        output = StringIO()
        with patch("sys.stdout", output):
            main.main()

        self.assertIn("Result: 4.0", output.getvalue())
        self.assertEqual(mocked_input.call_count, 3)

    @patch("builtins.input", side_effect=["abc", "+", "2"])
    def test_main_rejects_nonnumeric_input(self, mocked_input):
        output = StringIO()
        with patch("sys.stdout", output):
            main.main()

        self.assertIn("Please enter numeric values for both numbers.", output.getvalue())
        self.assertEqual(mocked_input.call_count, 3)


if __name__ == "__main__":
    unittest.main()
