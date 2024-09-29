import unittest
from long_div import stupid_long_div


class TestStupidLongDiv(unittest.TestCase):

    def test_normal_division(self):
        quotient, remainder = stupid_long_div(1234, 56)
        self.assertEqual(quotient, 22)
        self.assertEqual(remainder, 2)

    def test_division_by_one(self):
        quotient, remainder = stupid_long_div(5678, 1)
        self.assertEqual(quotient, 5678)
        self.assertEqual(remainder, 0)

    def test_division_by_itself(self):
        quotient, remainder = stupid_long_div(42, 42)
        self.assertEqual(quotient, 1)
        self.assertEqual(remainder, 0)

    def test_large_numbers(self):
        quotient, remainder = stupid_long_div(1000000, 7)
        self.assertEqual(quotient, 142857)
        self.assertEqual(remainder, 1)

    def test_division_by_zero(self):
        result = stupid_long_div(100, 0)
        self.assertEqual(result, "Error: Division by zero")

    def test_remainder_larger_than_divisor(self):
        quotient, remainder = stupid_long_div(100, 30)
        self.assertEqual(quotient, 3)
        self.assertEqual(remainder, 10)


if __name__ == "__main__":
    unittest.main()
