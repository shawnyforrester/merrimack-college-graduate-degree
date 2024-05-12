import unittest
import recursive_binary

class TestRecursiveBinary(unittest.TestCase):
    
    def test_binary_0(self):
        self.assertAlmostEqual(recursive_binary.binary(10), 4)

    def test_binary_1(self):
        self.assertAlmostEqual(recursive_binary.binary(256), 9)

    def test_binary_2(self):
        self.assertEqual(recursive_binary.binary(750), 10)

    

if __name__ == '__main__':
    unittest.main()