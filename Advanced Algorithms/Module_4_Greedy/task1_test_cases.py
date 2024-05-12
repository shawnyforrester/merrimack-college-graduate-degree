"""unit tests for task1.py"""

import unittest
from task1_egyptian_fractions import egyptian
#imported to capture the print statements
# from io import StringIO
# import sys


class TestEgypitan(unittest.TestCase):  

    # original_stdout = sys.stdout
    # sys.stdout = StringIO()  

#test case 1 when n = 5 and d = 6
    def test_egyptian_1(self):

        
        # actual_output = sys.stdout.getvalue()
        # sys.stdout = self.original_stdout
        expected_output = "The Egyptian Fractionof 5/6\n1/2,1/3\n"
        self.assertAlmostEqual(egyptian (5,6), expected_output)

#test case 2 when n = 7 and d = 15
    def test_egyptian_2(self):
        
        # actual_output = sys.stdout.getvalue()
        # sys.stdout = self.original_stdout
        expected_output = "The Egyptian Fractionof 7/15\n1/3,1/8,1/120\n"
        self.assertAlmostEqual(egyptian (7,15), expected_output)

#test case 3 when n = 23 and d = 34
    def test_egyptian_3(self):
        
        # actual_output = sys.stdout.getvalue()
        # sys.stdout = self.original_stdout
        expected_output = "The Egyptian Fractionof 23/34\n1/2,1/6,1/102\n"
        self.assertAlmostEqual(egyptian (23,34), expected_output)
        

#test case 4 when n = 121 and d = 321
    def test_egyptian_4(self):
        
        # actual_output = sys.stdout.getvalue()
        # sys.stdout = self.original_stdout
        expected_output = "The Egyptian Fractionof 121/321\n1/3,1/1538,1/4729350\n"
        self.assertAlmostEqual(egyptian (121,321), expected_output)
        

#test case 5 when n = 5 and d = 123
    def test_egyptian_5(self):
        
        # actual_output = sys.stdout
        # sys.stdout = self.original_stdout
        expected_output = "The Egyptian Fractionof 5/123\n1/25,1/1538,1/4729350\n"
        self.assertAlmostEqual(egyptian (5,123), expected_output)
        

if __name__ == '__main__':
    unittest.main()
