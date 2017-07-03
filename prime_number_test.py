import unittest
from prime_number import prime_number


class TestForPrimeNumbers(unittest.TestCase):
    def test_raises_error_when_arg_is_a_string(self):
        self.assertRaises(ValueError, prime_number, "2")

    def test_function_returns_a_list(self):
        self.assertEqual(type(prime_number(10)), list, "A list is not returned")

    def test_empty_list_returned_when_arg_is_negative(self):
        self.assertEqual([], prime_number(-5), "Function should return an empty list")

    def test_function_returns_list_of_integers(self):
        self.assertTrue(all(isinstance(n, int) for n in (prime_number(15))), "Returned list has non-integer elements")

    def test_function_returns_correct_result(self):
        self.assertEqual([2, 3, 5, 7], prime_number(10))


if __name__ == '__main__':
    unittest.main()
