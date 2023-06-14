import unittest
import bubble_sort


class TestBubbleSort(unittest.TestCase):

    def test_bubble_sort_1(self):
        A4 = [44, 63, 77, 17, 20, 99, 84, 6, 39, 52]
        bubble_sort.BubbleSort(A4)
        self.assertEqual(A4, [6, 17, 20, 39, 44, 52, 63, 77, 84, 99])

    def test_bubble_sort_2(self):
        A5 = [52, 84, 6, 39, 20, 77, 17, 99, 44, 63]
        bubble_sort.BubbleSort(A5)
        self.assertAlmostEquals(A5, [6, 17, 20, 39, 44, 52, 63, 77, 84, 99])

    def test_bubble_sort_3(self):
        A6 = [6, 17, 20, 39, 44, 52, 63, 77, 84, 99]
        bubble_sort.BubbleSort(A6)
        self.assertAlmostEquals(A6, [6, 17, 20, 39, 44, 52, 63, 77, 84, 99])


if __name__ == '__main__':
    unittest.main()
