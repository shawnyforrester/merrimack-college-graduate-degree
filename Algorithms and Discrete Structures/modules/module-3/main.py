"""Main function that creates a tree and reads the numbers.txt file
and creates a graph from the tree"""

#import the tree class
from tree_numbers import Tree

def read_data():
    """Reads the data from the numbers.txt file and returns it as a list"""
    with open("numbers.txt", "r") as f:
        data = f.read().splitlines()
    return data

def main():
    data = read_data()
    tree = Tree(data)
    #read the numbers.txt file
    with open("numbers.txt", "r") as f:
        #This creates a tree with the numbers in the file (1-31)
        for number in f:            
            tree.insert(int(number))    
    tree.printInorder()
    tree.printPreorder()
    tree.printPostorder()
    print(tree.check_level(2))#checks the depth of a particular value       
     
    #create a graph from the tree
    tree.print_matrix()
        
    
    
    
if __name__ == "__main__":
    main()     