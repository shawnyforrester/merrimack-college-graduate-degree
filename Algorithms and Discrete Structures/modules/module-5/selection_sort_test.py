import unittest
import selection_sort


class TestSelectionSort(unittest.TestCase):

    def test_selection_sort_1(self):
        A1 = [63, 44, 17, 77, 20, 6, 99, 84, 52, 39]
        selection_sort.SelectionSort(A1)
        self.assertEqual(A1, [6, 17, 20, 39, 44, 52, 63, 77, 84, 99])

    def test_selection_sort_2(self):
        A2 = [84, 52, 39, 6, 20, 17, 77, 99, 63, 44]
        selection_sort.SelectionSort(A2)
        self.assertEqual(A2, [6, 17, 20, 39, 44, 52, 63, 77, 84, 99])

    def test_selection_sort_3(self):
        A3 = [99, 84, 77, 63, 52, 44, 39, 20, 17, 6]
        selection_sort.SelectionSort(A3)
        self.assertEqual(A3, [6, 17, 20, 39, 44, 52, 63, 77, 84, 99])


if __name__ == '__main__':
    unittest.main()
