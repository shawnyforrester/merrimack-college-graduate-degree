"""Write a recursive algorithm to determine the location in a sorted array where a specified
searchkey is found. Unlike the algorithm in the class notes, this algorithm works with an array
that is sorted into DESCENDING order and the code should print out all the subscripts in the
array that were examined during the search. 

The sequence of elements that are examined is known as the “probe sequence”. Do not print out the “active” portion of the array, just the
subscript of the one “middle” element that is compared to the searchkey.

Your function should have the same four input parameters as the code in the class notes – array,
left subscript, right subscript, searchkey – and should return the subscript where the searchkey is
found (or the value None) using a return statement.

For example, if you were searching for 27 in the array A = [50, 41, 27, 20, 17, 12, 5], the probe
sequence printed by the algorithm would be: 3, 1, 2 because you would look at A[3]=20, then
A[1]=41, then A[2]=27, and then you would stop because the searchkey was found.
b) Run your code on the problem instances:
In array [100, 87, 85, 80, 72, 67, 55, 50, 48, 42, 40, 31, 25, 22, 18]
search for 87
search for 48
search for 33
search for 10
"""

def recursive_array_search(array, left, right, searchkey):
    if left > right:
        return None
    else:
        middle = (left + right) // 2
        print(middle)
        if array[middle] == searchkey:
            return middle
        elif array[middle] < searchkey:
            return recursive_array_search(array, left, middle - 1, searchkey)
        else:
            return recursive_array_search(array, middle + 1, right, searchkey)

def main():
    print("*********** Recursive Array Search ***********")
    print("****Search for 87****", "\n", "Probe Sequence: ")
    print(recursive_array_search([100, 87, 85, 80, 72, 67, 55, 50, 48, 42, 40, 31, 25, 22, 18], 0, 14, 87))
    print("****Search for 48****", "\n", "Probe Sequence: ")
    print(recursive_array_search([100, 87, 85, 80, 72, 67, 55, 50, 48, 42, 40, 31, 25, 22, 18], 0, 14, 48))
    print("****Search for 33****", "\n", "Probe Sequence: ")
    print(recursive_array_search([100, 87, 85, 80, 72, 67, 55, 50, 48, 42, 40, 31, 25, 22, 18], 0, 14, 33))
    print("****Search for 10****", "\n", "Probe Sequence: ")
    print(recursive_array_search([100, 87, 85, 80, 72, 67, 55, 50, 48, 42, 40, 31, 25, 22, 18], 0, 14, 10))

if __name__ == "__main__":
    main()