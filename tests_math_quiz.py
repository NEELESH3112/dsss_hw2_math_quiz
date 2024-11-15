import unittest
from math_quiz import generate_number, choose_operator, calculate

class TestMathGame(unittest.TestCase):

    def test_generate_number(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = generate_number(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_choose_operator(self):
        # Test if the operator returned is one of the expected ones
        operators = ['+', '-', '*', '/', '%']
        for _ in range(1000):  # Test multiple times to check randomness
            operator = choose_operator()
            self.assertIn(operator, operators)

    def test_calculate(self):
        test_cases = [
            (5, 2, '+', '5 + 2', 7),          # Addition
            (31, 12, '-', '31 - 12', 19),     # Subtraction
            (89, 11, '*', '89 * 11', 979),    # Multiplication
            (75, 25, '/', '75 / 25', 3),      # Division
            (6, 0, '/', '6 / 0', "Undefined"), # Division by zero
            (5, 2, '%', '5 % 2', 1),          # Modulus
            (57, 0, '%', '57 % 0', "Undefined"),  # Modulus by zero
        ]
        for num1, num2, operator, expected_problem, expected_answer in test_cases:
            problem, answer = calculate(num1, num2, operator)
            self.assertEqual(problem, expected_problem)
            self.assertEqual(answer, expected_answer)

if __name__ == "__main__":
    unittest.main()
<<<<<<< HEAD

=======
>>>>>>> 46a34ad07c3aa74b1cb4aa79154fc8cdc813fad2
