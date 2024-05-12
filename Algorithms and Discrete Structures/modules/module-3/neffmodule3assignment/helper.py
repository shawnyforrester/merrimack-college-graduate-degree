class Helper:
    '''
    A class of helper methods.
    '''
    def __init__(self):
        # This class has no instances. It is merely used to encapsulate Helper methods used throughout the program.
        pass

    def generateEmptyGraph(n):
        '''
        a method that takes a Tree object and a value; searches the
        tree for that value and returns the value of the parent. This method returns False if 
        the value is the value of the Root node or if the value does not appear in the tree.
        '''
        graph = []
        for i in range(n):
            row = []
            for j in range(n):
                row.append(0)
            graph.append(row)
        return graph

    def printGraph(g):
        '''
        A method that accepts a matrix and prints out each row one at a time.
        This method returns nothing.
        '''
        for r in g:
            print(r)


