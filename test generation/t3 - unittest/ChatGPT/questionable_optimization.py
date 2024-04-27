import unittest
# from parameterized import parameterized
from expression_calculator import calculate_expression

class TestCalculateExpression(unittest.TestCase):
    
    @parameterized.expand([
        ("Скільки буде 2 плюс 3?", 5),
        ("Скільки буде 5 мінус 3?", 2),
        ("Скільки буде 4 помножити на 2?", 8),
        ("Скільки буде 10 поділити на 2?", 5),
    ])
    def test_valid_expressions(self, expression, expected_result):
        self.assertEqual(calculate_expression(expression), expected_result)
        
    @parameterized.expand([
        ("Скільки буде п'ять плюс три?", 'Неправильний вираз!'),
        ("Скільки буде три плюс?", 'Неправильний вираз!'),
        ("Відняти п'ять плюс три?", 'Неправильний вираз!'),
        ("Скільки буде 10 поділити на 0?", 'Неправильний вираз!'),
        ("", 'Неправильний вираз!'),
        ("Скільки буде 2 плюс 3", 'Неправильний вираз!'),
        ("Скільки буде підняти в степінь 2 до 3?", 'Неправильний вираз!'),
        ("Скільки буде 5?", 'Неправильний вираз!'),
        ("Скільки буде 5?", 'Неправильний вираз!'),
    ])
    def test_invalid_expressions(self, expression, expected_result):
        self.assertEqual(calculate_expression(expression), expected_result)

if __name__ == '__main__':
    unittest.main()
