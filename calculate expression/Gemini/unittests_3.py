import unittest

from Gemini.expression_calculator_redone import calculate_expression

class CalculateExpressionTest(unittest.TestCase):

    def test_simple_addition(self):
        self.assertEqual(calculate_expression('Скільки буде 8 додати 3 ?'), 11)

    def test_simple_subtraction(self):
        self.assertEqual(calculate_expression('Скільки буде 7 відняти 3 ?'), 4)

    def test_simple_multiplication(self):
        self.assertEqual(calculate_expression('Скільки буде 7 помножити на 3 ?'), 21)

    def test_simple_division(self):
        self.assertEqual(calculate_expression('Скільки буде 12 поділити на 3 ?'), 4)

    def test_complex_expression(self):
        self.assertEqual(
            calculate_expression('Скільки буде 10 поділити на -2 додати 11 мінус -3 ?'), 9
        )

    def test_invalid_expression_missing_start(self):
        self.assertEqual(calculate_expression('10 додати 5 ?'), 'Неправильний вираз!')

    def test_invalid_expression_missing_end(self):
        self.assertEqual(calculate_expression('Скільки буде 10 додати 5'), 'Неправильний вираз!')

    def test_invalid_expression_extra_text(self):
        self.assertEqual(calculate_expression('Скільки буде 10 додати 5 Це правильно ?'), 'Неправильний вираз!')

    def test_invalid_expression_missing_number(self):
        self.assertEqual(calculate_expression('Скільки буде додати 5 ?'), 'Неправильний вираз!')

    def test_invalid_expression_missing_operator(self):
        self.assertEqual(calculate_expression('Скільки буде 10 5 ?'), 'Неправильний вираз!')

if __name__ == "__main__":
    unittest.main()
