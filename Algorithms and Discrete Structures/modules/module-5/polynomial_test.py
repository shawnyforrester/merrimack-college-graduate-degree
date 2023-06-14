import unittest
import polynomial


class TestPolynomial(unittest.TestCase):

    def test_power_function_1(self):
        self.assertEqual(polynomial.power_function(2, 3), 8)

    def test_power_function_2(self):
        self.assertEqual(polynomial.power_function(0, 0), 1)

    def test_polynomial_function_1(self):
        self.assertAlmostEquals(polynomial.polynomial_function(
            [12.3, 40.7, -9.1, 7.7, 6.4, 0, 8.9], 5.4), 485527.79)


if __name__ == '__main__':
    unittest.main()
