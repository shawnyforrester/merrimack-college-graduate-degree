"""Main function that creates a tree and reads the numbers.txt file
and creates a graph from the tree"""

# import the tree class
from tree_numbers import Tree


def read_data():
    """Reads the data from the numbers.txt file and returns it as a list"""
    data = []
    with open("numbers.txt", "r") as f:
        for line in f:
            data.append(line.strip())
    return data


def main():
    data = read_data()
    tree = Tree(data)
    # read the numbers.txt file
    with open("numbers.txt", "r") as f:
        # This creates a tree with the numbers in the file (1-31)
        for number in f:
            tree.insert(int(number))
    tree.printInorder()
    tree.printPreorder()
    tree.printPostorder()
    print(tree.check_level(8))  # checks the depth of a particular value

    #create a graph from the tree
    tree.create_adjacency_matrix()


if __name__ == "__main__":
    main()
