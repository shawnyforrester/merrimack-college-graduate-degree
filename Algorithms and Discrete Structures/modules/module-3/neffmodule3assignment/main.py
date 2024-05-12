from tree import Node
from tree import Tree
from helper import Helper

def main():
    '''    
    To run the other test cases, change the file name in line X. 
    numbers.txt: the test case from the project description
    numbers2.txt: the test case from slide 14 of Module 3
    numbers3.txt: five numbers decreasing by one; should result in a downward diagnal line of '1's
    numbers4.txt: one number tree; should result in a matrix of one row, one column with a single 0. 
    numbers5.txt: a perfect tree of height 2.
    '''
    # Open whichever file you want to read the integer values.
    numFile = open("numbers.txt", "r")
    # Save the number strings in an array using the readlines() method.
    numbers = numFile.readlines()
    # Instantiate an empty array, nums.
    nums = []
    # Iterate through the number strings, converting each to an integer and appending each integer to nums.
    for n in numbers:
        n = int(n)
        nums.append(n)
    # Instantiate an empty Tree object, t.
    t = Tree()
    # Iterate through nums, inserting each into t.
    for num in nums:
        t.insert(num)

    # Save a matrix of 0s as variable graph using the 
    # helper method generateEmptyGraph and passing 
    # the length of nums in as an argument.
    graph = Helper.generateEmptyGraph(len(nums))
    # Change graph to the return value of t.editGraphPreorder(graph)
    graph = t.editGraphPreorder(graph)
    # Print the resulting adjaceny matrix using the helper method pringGraph(graph).
    Helper.printGraph(graph)

if __name__ == '__main__':
    main()