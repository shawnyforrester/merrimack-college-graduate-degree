""" Write a recursive decrease-and-conquer algorithm to calculate the maximum element in a non-empty array of real numbers. Your algorithm should work by comparing the last element in the
array with the maximum of the “remaining front end” of the array.
For example, to find the largest element in the array <5, 13, 9, 10> your algorithm should call 
itself to find the maximum of <5, 13, 9> and return either 10 or the result of the recursive call, 
whichever is larger. 
Parameters and return: Your function call should call should be 
Maximum(A, right) 
where the two input parameters are the array and right index. With these input parameters, the 
function should return the maximum array element from A[0] to A[right]. Using a return 
statement, return the value of the array element, not the index where it occurs in the array. 
Do not use Python\s built-in max() function. 
Do not rearrange the elements of the array by sorting or partially sorting them. 
Do not use any loops. 
You can assume that the array has at least one element in it. """

def max_array_element(A, right):
    if right == 0:
        return A[0]
    else:
        if A[right] > max_array_element(A, right-1):
            return A[right]
        else:
            return max_array_element(A, right-1)

def main():
    A = [17, 62, 49, 73, 26, 51]
    print(max_array_element(A, len(A)-1))

main()
            