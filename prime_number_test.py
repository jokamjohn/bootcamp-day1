import unittest
from prime_number import prime_number


class TestForPrimeNumbers(unittest.TestCase):
    def test_raises_error_when_an_is_a_string(self):
        self.assertRaises(ValueError, prime_number, "2")

    def test_function_returns_a_list(self):
        self.assertEqual(type(list), prime_number(10), "A list is not returned")


