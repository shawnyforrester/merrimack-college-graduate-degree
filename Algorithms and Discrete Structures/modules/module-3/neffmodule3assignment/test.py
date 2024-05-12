import unittest
from tree import Node
from tree import Tree
from helper import Helper

class Module3(unittest.TestCase):
    '''
    This test module tests the three most critical methods of this program:

    1. generateParaentData - a method that takes a Tree object and a value; searches the
    tree for that value and returns the value of the parent. This method returns False if 
    the value is the value of the Root node or if the value does not appear in the tree.

    2. generateEmtpyGraph - a method which takes an integer value, n, and returns an n by n matrix filled
    with 0s.

    3. editGraphPreorder - the main 'meat' of the program; a tree instance method which accepts a graph; the method 
    visits the nodes of the tree in preorder and edits the graph in such a way that it is changed to an adjaceny matrix/graph 
    representation of the tree where the weights are the absolute value of the difference between the two nodes' data.
    '''


    # TESTS FOR GENERATEPARENTDATA - A static method to generate
    # the data of the parent node. 

    # Test that the tree root value will enter when looking for a node in level 1.
    def testGenerateParentData1(self):
        numFile = open("numbers.txt", "r")
        numbers = numFile.readlines()
        nums = []
        for n in numbers:
            n = int(n)
            nums.append(n)
        t = Tree()
        for num in nums:
            t.insert(num)
        self.assertEqual(Tree.generateParentData(t.Root,12),34)

    # Test that the parent node data from level one will be returned when 
    # checking for parent data of a number in level two, of greater value than the parent
    def testGenerateParentData2(self):
        numFile = open("numbers.txt", "r")
        numbers = numFile.readlines()
        nums = []
        for n in numbers:
            n = int(n)
            nums.append(n)
        t = Tree()
        for num in nums:
            t.insert(num)
        self.assertEqual(Tree.generateParentData(t.Root,13),12)

    # Test that the parent node data from level one will be returned when 
    # checking for parent data of a number in level two, of lesser value than the parent
    def testGenerateParentData3(self):
        numFile = open("numbers.txt", "r")
        numbers = numFile.readlines()
        nums = []
        for n in numbers:
            n = int(n)
            nums.append(n)
        t = Tree()
        for num in nums:
            t.insert(num)
        self.assertEqual(Tree.generateParentData(t.Root,8),12)

    # Test that the method returns False when the Tree Root value is entered as the second parameter.
    def testGenerateParentData4(self):
        numFile = open("numbers.txt", "r")
        numbers = numFile.readlines()
        nums = []
        for n in numbers:
            n = int(n)
            nums.append(n)
        t = Tree()
        for num in nums:
            t.insert(num)
        self.assertFalse(Tree.generateParentData(t.Root,34))

    # Test that the method returns False when a value not found in the tree is entered as the second parameter.
    def testGenerateParentData5(self):
        numFile = open("numbers.txt", "r")
        numbers = numFile.readlines()
        nums = []
        for n in numbers:
            n = int(n)
            nums.append(n)
        t = Tree()
        for num in nums:
            t.insert(num)
        self.assertFalse(Tree.generateParentData(t.Root,60))

    # Test that the method returns False when a value not found in the tree is entered as the second parameter.
    def testGenerateParentData6(self):
        numFile = open("numbers.txt", "r")
        numbers = numFile.readlines()
        nums = []
        for n in numbers:
            n = int(n)
            nums.append(n)
        t = Tree()
        for num in nums:
            t.insert(num)
        self.assertFalse(Tree.generateParentData(t.Root,1))

    # Test that the method returns False when a value not found in the tree is entered as the second parameter.
    def testGenerateParentData7(self):
        numFile = open("numbers.txt", "r")
        numbers = numFile.readlines()
        nums = []
        for n in numbers:
            n = int(n)
            nums.append(n)
        t = Tree()
        for num in nums:
            t.insert(num)
        self.assertFalse(Tree.generateParentData(t.Root,14))

    # TEST FOR HELPER.GENERATEEMPTYGRAPH

    def testGenerateEmptyGraph1(self):
        graph = Helper.generateEmptyGraph(3)
        self.assertEqual(graph,
        [
            [0,0,0],
            [0,0,0],
            [0,0,0]
        ]
        )

    def testGenerateEmptyGraph2(self):
        graph = Helper.generateEmptyGraph(3)
        self.assertNotEqual(graph,
        [
            [0,0],
            [0,0],
            [0,0]
        ]
        )
    # TESTS FOR TREE.EDITGRAPHPREORDER
    # Test that the example adjacency graph from the project returns correctly.
    def testEditGraphPreorder1(self):
        numFile = open("numbers.txt", "r")
        numbers = numFile.readlines()
        nums = []
        for n in numbers:
            n = int(n)
            nums.append(n)
        t = Tree()
        for num in nums:
            t.insert(num)
        graph = Helper.generateEmptyGraph(len(nums))
        graph = t.editGraphPreorder(graph)
        self.assertEqual(
            [
            [0,22,0,0,21],
            [0,0,4,1,0],
            [0,0,0,0,0],
            [0,0,0,0,0],
            [0,0,0,0,0]
            ],
            graph
        )

    # Test that the graph found on Module 3 Slide 14 returns correctly.
    def testEditGraphPreorder2(self):
        numFile = open("numbers2.txt", "r")
        numbers = numFile.readlines()
        nums = []
        for n in numbers:
            n = int(n)
            nums.append(n)
        t = Tree()
        for num in nums:
            t.insert(num)
        graph = Helper.generateEmptyGraph(len(nums))
        graph = t.editGraphPreorder(graph)
        self.assertEqual(
            [
                [0, 5, 0, 0, 0, 0, 0, 0, 0, 11, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 10, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 5, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 4, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 0, 4, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 8, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 2],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            ],
            graph
        )
        
    # Test that a five node tree, all differing values by one returns correctly.
    def testEditGraphPreorder3(self):
        numFile = open("numbers3.txt", "r")
        numbers = numFile.readlines()
        nums = []
        for n in numbers:
            n = int(n)
            nums.append(n)
        t = Tree()
        for num in nums:
            t.insert(num)
        graph = Helper.generateEmptyGraph(len(nums))
        graph = t.editGraphPreorder(graph)
        self.assertEqual(
            [
            [0,1,0,0,0],
            [0,0,1,0,0],
            [0,0,0,1,0],
            [0,0,0,0,1],
            [0,0,0,0,0]
            ],
            graph
        )

    # Test that a one node tree, returns a graph of [[0]]
    def testEditGraphPreorder4(self):
        numFile = open("numbers4.txt", "r")
        numbers = numFile.readlines()
        nums = []
        for n in numbers:
            n = int(n)
            nums.append(n)
        t = Tree()
        for num in nums:
            t.insert(num)
        graph = Helper.generateEmptyGraph(len(nums))
        graph = t.editGraphPreorder(graph)
        self.assertEqual(
            [
            [0]
            ],
            graph
        )
    
    def testGeneratePreorderIndex1(self):
        numFile = open("numbers2.txt", "r")
        numbers = numFile.readlines()
        nums = []
        for n in numbers:
            n = int(n)
            nums.append(n)
        t = Tree()
        for num in nums:
            t.insert(num)
        self.assertEqual(t.generatePreorderIndex(25),0)

    def testGeneratePreorderIndex2(self):
        numFile = open("numbers2.txt", "r")
        numbers = numFile.readlines()
        nums = []
        for n in numbers:
            n = int(n)
            nums.append(n)
        t = Tree()
        for num in nums:
            t.insert(num)
        self.assertEqual(t.generatePreorderIndex(20),1)

    def testGeneratePreorderIndex3(self):
        numFile = open("numbers2.txt", "r")
        numbers = numFile.readlines()
        nums = []
        for n in numbers:
            n = int(n)
            nums.append(n)
        t = Tree()
        for num in nums:
            t.insert(num)
        self.assertEqual(t.generatePreorderIndex(45),15)

if __name__ == '__main__':
    unittest.main()


    