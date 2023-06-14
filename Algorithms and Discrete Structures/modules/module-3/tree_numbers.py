"""Create a program that reads a list of numbers from a file and creates 
a binary search tree from the numbers."""


import math


class Node:
    def __init__(self, value=None):
        self.data = value
        self.left = None
        self.right = None


class Tree:
    def __init__(self, data_set):
        # self.iteration = 0
        self.data_set = data_set
        # if (value == None):
        #     self.root = None
        # else:
        self.root = Node()

    def insert(self, value):
        def insert_here(node, value):
            if (node.data > value):  # if the node data is greater than the value assign it the left
                if (node.left == None):
                    node.left = Node(value)
                else:
                    insert_here(node.left, value)

            elif (node.data < value):
                if (node.right == None):
                    node.right = Node(value)
                else:
                    insert_here(node.right, value)

        if (self.root == None):  # In case the tree is empty
            self.root = Node(value)
        else:
            if (self.root.data > value):
                if (self.root.left == None):
                    self.root.left = Node(value)
                else:
                    insert_here(self.root.left, value)
            elif (self.root.data < value):
                if (self.root.right == None):
                    self.root.right = Node(value)
                else:
                    insert_here(self.root.right, value)

    def check_level(self, d):
        def __check__(n, d):
            level = 0
            if (n == None):
                return "Not found"
            while (n.data != d):
                if (n.data > d):
                    level += 1
                    n = n.left
                elif (n.data < d):
                    level += 1
                    n = n.right
            if n.data == d:
                return "The level of this node is: " + str(level)
        return __check__(self.root, d)

    # function to print in order
    def printInorder(self):
        # recursive function to print the tree inorder
        def __visit__(n):
            if n is not None:
                __visit__(n.left)
                print(n.data, end=" ")
                __visit__(n.right)

        print("\n--------")
        __visit__(self.root)
        print("\n--------")

    # function to print preorder

    def printPreorder(self):
        def __visit__(n, h):
            if n is not None:
                print("---"*h, n.data)
                __visit__(n.left, h+1)
                __visit__(n.right, h+1)
        print("^^^^^^^^^^")
        __visit__(self.root, 0)
        print("^^^^^^^^^^")
    # function to print postorder

    def printPostorder(self):
        def __visit__(n, h):
            if n is not None:
                __visit__(n.left, h+1)
                __visit__(n.right, h+1)
                print("---"*h, n.data)
        print("==========")
        __visit__(self.root, 0)
        print("==========")

    # def create_matrix(self, number):
    #     matrix = [[0 for i in range(number)] for j in range(number)]
    #     return matrix

    # def print_matrix(self):
    #     matrix  = self.create_matrix(len(self.data))

    #     def __visit__(n, matrix):
    #         if n is not None:

    #             if n.left is not None or n.right is not None:
    #                 current = n.data
    #                 input_data = self.data

    #                 try:
    #                     current_left = n.left.data
    #                     left_weight = abs(current - current_left)
    #                     index_left = input_data.index(current_left)
    #                     matrix[self.iteration][index_left] = left_weight
    #                 except:
    #                     pass

    #                 try:
    #                     current_right = n.right.data
    #                     right_weight = abs(current - current_right)
    #                     index_right = input_data.index(current_right)
    #                     matrix[self.iteration][index_right] = right_weight
    #                 except:
    #                     pass
    #                 self.iteration += 1
    #         else:
    #             self.iteration += 1

    #         __visit__(n.left, matrix)
    #         __visit__(n.right, matrix)

    #     print("\n----------")
    #     __visit__(self.root, matrix)
    #     print(matrix)
    #     print("\n----------")

    def create_adjacency_matrix(self):
    # Initialize a 2D matrix of size 31x31 filled with zeros
        adjacency_matrix = [[0] * len(self.data_set) for _ in range(len(self.data_set))]

    # Helper function to fill the adjacency matrix recursively
        def fill_adjacency_matrix(node): 
            if node.left is not None or node.right is not None:
                current = node                      
                   
            if current.data < len(self.data_set):
                adjacency_matrix[current.data][current.data.left] = abs(current.data - current.left.data)
                adjacency_matrix[current.data][current.data.right] = abs(current.data - current.right.data)                
                fill_adjacency_matrix(current.left)
                fill_adjacency_matrix(current.right)

    # Start filling the adjacency matrix from the root node at index 0
        fill_adjacency_matrix(self.root)

    # Print the adjacency matrix
        for row in adjacency_matrix:
            print(' '.join(map(str, row)))

# Call the function to create and print the adjacency matrix
    # create_adjacency_matrix()

""""
vist(self.root)
    if node.left is not None or node.right is not None:
        current = node.data
        x coordinate is current.data
        y coordinate is the child node data (either current.left.data or current.right.data))
        The value of the edge is current.data - current.left.data or current.data - current.right.data
        The index of [x][y] = value of the edge"""