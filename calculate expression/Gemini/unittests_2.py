import unittest

from Gemini.expression_calculator_redone import calculate_expression

class ExpressionCalculatorTest(unittest.TestCase):

    def test_simple_addition(self):
        self.assertEqual(calculate_expression("Скільки буде 8 додати 3?"), 11)

    def test_simple_subtraction(self):
        self.assertEqual(calculate_expression("Скільки буде 7 відняти 3?"), 4)

    def test_simple_multiplication(self):
        self.assertEqual(calculate_expression("Скільки буде 7 помножити на 3?"), 21)

    def test_simple_division(self):
        self.assertEqual(calculate_expression("Скільки буде 12 поділити на 3?"), 4)

    def test_complex_expression(self):
        self.assertEqual(
            calculate_expression("Скільки буде 10 поділити на -2 додати 11 мінус -3?"), 9
        )

    def test_leading_zero(self):
        self.assertEqual(calculate_expression("Скільки буде 0 додати 5?"), 5)

    def test_multiple_spaces(self):
        self.assertEqual(calculate_expression("Скільки буде 2  відняти  3?"), -1)

    def test_empty_space_around_operator(self):
        self.assertEqual(calculate_expression("Скільки буде 2 + 3?"), 5)

    def test_negative_number(self):
        self.assertEqual(calculate_expression("Скільки буде -5 додати 3?"), -2)

        self.assertEqual(calculate_expression("Скільки буде 10 відняти -2?"), 12)

    def test_division_by_one(self):
        self.assertEqual(calculate_expression("Скільки буде 10 поділити на 1?"), 10)

    def test_large_numbers(self):
        self.assertEqual(
            calculate_expression("Скільки буде 1000000000 додати 100000000?"), 1001000000
        )

    def test_case_insensitive(self):
        self.assertEqual(calculate_expression("Скільки буде 2 ПЛЮС 3?"), 5)

    def test_extra_text_after_expression(self):
        self.assertEqual(
            calculate_expression("Скільки буде 2 додати 3? Це правильно."), 5
        )

    def test_empty_expression(self):
        self.assertEqual(calculate_expression(""), "Неправильний вираз!")


if __name__ == "__main__":
    unittest.main()
