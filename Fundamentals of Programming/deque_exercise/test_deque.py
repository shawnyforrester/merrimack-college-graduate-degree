import unittest
from forrester6 import*

class TestAppendLeft(unittest.TestCase):

    def test_left(self):
        deque = Deque()
         
        item = 'here'
        deque.Add_Left(item)
        next_item = 'everywhere'
        self.assertAlmostEqual(deque.Add_Left(next_item),['everywhere', 'here'])
        
    
class TestAppendRight(unittest.TestCase):

    def test_right(self):
        deque = Deque()

        item = 'here'
        deque.Add_Right(item)
        
        next_item = 'everywhere'
        self.assertAlmostEqual(deque.Add_Right(next_item), ['here', 'everywhere'])
        
        
class Delete_Item(unittest.TestCase):
    
    def deleteItem(self):
        deque = Deque()
        
        item = 'here'
        deque.Add_Left(item)

        next_item = 'everywhere'
        deque.Add_Left(next_item)
        self.assertAlmostEqual(deque.Remove_item(next_item), ['here'])
        

if __name__ == '__main__':
    unittest.main()
