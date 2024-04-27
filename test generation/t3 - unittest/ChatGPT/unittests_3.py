import unittest
from ChatGPT.expression_calculator_redone import calculate_expression

class TestCalculateExpression(unittest.TestCase):
    
    def test_valid_expressions(self):
        self.assertEqual(calculate_expression("Скільки буде додати 2 плюс 3?"), 5)
        self.assertEqual(calculate_expression("Скільки буде відняти 5 мінус 3?"), 2)
        self.assertEqual(calculate_expression("Скільки буде помножити на 4 поділити на 2?"), 2)
        self.assertEqual(calculate_expression("Скільки буде поділити на 10 плюс 5?"), 0.5)
        
    def test_invalid_expressions(self):
        self.assertEqual(calculate_expression("Скільки буде додати п'ять плюс три?"), 'Неправильний вираз!')
        self.assertEqual(calculate_expression("Скільки відняти три плюс?"), 'Неправильний вираз!')
        self.assertEqual(calculate_expression("Відняти п'ять плюс три?"), 'Неправильний вираз!')
        
    def test_division_by_zero(self):
        self.assertEqual(calculate_expression("Скільки буде поділити на 0 плюс 5?"), 'Неправильний вираз!')
        
    def test_empty_expression(self):
        self.assertEqual(calculate_expression(""), 'Неправильний вираз!')
        
    def test_expression_without_question_mark(self):
        self.assertEqual(calculate_expression("Скільки буде додати 2 плюс 3"), 'Неправильний вираз!')
        
    def test_invalid_operator(self):
        self.assertEqual(calculate_expression("Скільки буде підняти в степінь 2 до 3?"), 'Неправильний вираз!')
        
    def test_single_digit_expression(self):
        self.assertEqual(calculate_expression("Скільки буде додати 5?"), 'Неправильний вираз!')
        
    def test_no_operation_expression(self):
        self.assertEqual(calculate_expression("Скільки буде 5?"), 'Неправильний вираз!')

if __name__ == '__main__':
    unittest.main()