from re import I


class Node:
    '''
    Node class representing a node in a binary tree.
    '''
    def __init__(self, data):
        self.Data = data
        self.Left = None
        self.Right = None

class Tree:
    '''
    Tree class used to represent binary trees.
    '''
    def __init__(self, data=None):
        if (data == None):
            self.Root = None
        else:
            self.Root = Node(data)

    # Method to inserting data as a new node in the appropriate place in the binary tree.
    def insert(self, d):
        def __insertHere__(n, d):
            if (n.Data > d):
                if (n.Left == None):
                    n.Left = Node(d)
                else: 
                    __insertHere__(n.Left, d)
            elif (n.Data < d):
                if (n.Right == None):
                    n.Right = Node(d)
                else:
                    __insertHere__(n.Right, d)
        if (self.Root == None):
            self.Root = Node(d)
        else:
            if (self.Root.Data > d):
                if (self.Root.Left == None):
                    self.Root.Left = Node(d)
                else:
                    __insertHere__(self.Root.Left, d)
            elif (self.Root.Data < d):
                if (self.Root.Right == None):
                    self.Root.Right = Node(d)
                else:
                    __insertHere__(self.Root.Right, d)


    def editGraphPreorder(self, graph):
        '''
        A Tree instance method that accepts a matrix as an argument.
        The method visits each node in preorder order, altering the matrix
        to become an adjacency matrix where the weight values represent the absolute value of the
        difference in data values between parent and child nodes. Nodes are "vertexed" in preorder index.
        '''
        i = 0  
        def __visit__(n, h):
            nonlocal i
            if (n != None):
                if (i == 0):
                        h = h-1
                        i += 1
                else:
                    # Most important line of the program. Sets the absolute difference (for the edge) to the graph with the 
                    # Coordinates of the parent index using the generatePreorderIndex on the parent node data,
                    # and the index, cycling through the nodes in preorder fashion.
                    graph[self.generatePreorderIndex(Tree.generateParentData(self.Root,n.Data))][i] = (abs(Tree.generateParentData(self.Root, n.Data)-n.Data))
                    i += 1   
                __visit__(n.Left, h+1)
                __visit__(n.Right, h+1)
        __visit__(self.Root, 0)
        return graph

    @staticmethod
    def generateParentData(root, value):
        '''
        A static method accepting a root node and a integer value as arguments.
        The method then searches through the tree and returns the data of the parent node of 
        the value, if such a value exists in the tree.
        The method returns False if the value is found in the Root node of the tree or if
        the value does not exists in the tree.
        '''
        if root.Data == value:
            return False
        if ((root.Left and root.Left.Data == value) or (root.Right and root.Right.Data == value)):
            return root.Data
        else:
            if (value < root.Data):
                if root.Left:
                    return Tree.generateParentData(root.Left, value)
            else:
                if root.Right:
                    return Tree.generateParentData(root.Right, value)
        return False

    def generatePreorderIndex(self, value):
        '''
        A tree instance method to return the preorder index of any node. 
        Input: a node value
        Output: the preorder index of that node (if it exists) in the Tree.
        '''
        arr = []
        def __visit__(n):
            nonlocal arr
            if (n!=None):
                arr.append(n.Data)
                __visit__(n.Left)
                __visit__(n.Right)
        __visit__(self.Root)
        return arr.index(value)

