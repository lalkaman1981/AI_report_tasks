import unittest
from ChatGPT.expression_calculator_redone import calculate_expression

class TestCalculateExpression(unittest.TestCase):

    def test_simple_addition(self):
        self.assertEqual(calculate_expression("Скільки буде 8 додати 3?"), 11)

    def test_complex_expression(self):
        self.assertEqual(calculate_expression("Скільки буде 7 додати 3 помножити на 5?"), 50)

    def test_negative_numbers(self):
        self.assertEqual(calculate_expression("Скільки буде 10 відняти 20?"), -10)

    def test_division(self):
        self.assertEqual(calculate_expression("Скільки буде 15 поділити на 3?"), 5)

    def test_invalid_expression(self):
        self.assertEqual(calculate_expression("Скільки буде 3 в кубі?"), 'Неправильний вираз!')

    def test_invalid_syntax(self):
        self.assertEqual(calculate_expression("Скільки буде 2 2 додати?"), 'Неправильний вираз!')

    def test_invalid_operation(self):
        self.assertEqual(calculate_expression("Скільки сезонів в році?"), 'Неправильний вираз!')

    def test_empty_expression(self):
        self.assertEqual(calculate_expression(""), 'Неправильний вираз!')

    def test_missing_operand(self):
        self.assertEqual(calculate_expression("Скільки буде мінус 5?"), 'Неправильний вираз!')

    def test_missing_operator(self):
        self.assertEqual(calculate_expression("Скільки буде 10 5?"), 'Неправильний вираз!')

    def test_divide_by_zero(self):
        self.assertEqual(calculate_expression("Скільки буде 10 поділити на 0?"), 'Неправильний вираз!')

    def test_single_digit(self):
        self.assertEqual(calculate_expression("Скільки буде 5?"), 5)

    def test_large_numbers(self):
        self.assertEqual(calculate_expression("Скільки буде 1000000 помножити на 2?"), 2000000)

    def test_case_insensitivity(self):
        self.assertEqual(calculate_expression("Скільки БУДЕ 10 додати 5?"), 15)

    def test_additional_spaces(self):
        self.assertEqual(calculate_expression("Скільки буде 8   додати   3?"), 11)

    def test_trailing_spaces(self):
        self.assertEqual(calculate_expression("Скільки буде 8 додати 3 ?  "), 11)

    def test_multiple_operators_in_line(self):
        self.assertEqual(calculate_expression("Скільки буде 8 додати 3 помножити на?"), 'Неправильний вираз!')

    def test_two_operators_in_row(self):
        self.assertEqual(calculate_expression("Скільки буде 8 додати помножити на 3?"), 'Неправильний вираз!')

    def test_negative_numbers(self):
        self.assertEqual(calculate_expression("Скільки буде -8 додати 3?"), -5)

if __name__ == '__main__':
    unittest.main()
