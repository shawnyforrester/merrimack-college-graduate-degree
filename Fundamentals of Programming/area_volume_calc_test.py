"""Unit testing the perimeter, area, and volume functions used in the respective classes"""
from forrester4 import*
import unittest

class TestPerimeter(unittest.TestCase):
        
    def test_Perimeter(self):
        p1 = Rectangle(3,4)
        self.assertAlmostEqual(p1.Perimeter(),14)
        
class TestArea(unittest.TestCase):
    def test_Area(self):
        a1 = Rectangle(3,4)
        self.assertAlmostEqual(a1.Area(),12)
        
class TestVolume(unittest.TestCase):
    def test_Volme(self):
        p2 = Parallelepiped(3,4,2)
        self.assertAlmostEqual(p2.Volume(),24)

if __name__ == '__main__':
    unittest.main
