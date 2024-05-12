"""Given two arrays of integers A with len(A) = n and len(B) = m, create a third array C
that includes all elements of A that are not in B. 
Example: With A = [6, 5, 2, 4] and B = [4, 3, 5], your algorithm should produce C = [6, 2]. 

Directions/requirements:
a) Write a brute force function that uses nested for loops to repeatedly check if each element in A
matches any of the elements in B. If the element from A does not match any element in B, then
copy it into the next available slot of array C.

Your function should have two input parameters (the sets A and B) and should return the set 
difference (the set C) through the return statement. Be sure to explain the inputs and outputs in 
your comments.

You can use the Python “in” operator to control the for loops, but do not use the Python “in” 
operator to test to see if an element of one set is in the other set. You may assume that in each 
array, each element is listed only once (there are no duplicates within the same array). Do not 
assume that either array is sorted and do not sort any of the arrays at any time. Number each line"""

def array_excluded_elements(A, B):
    C = []
    for i in range(len(A)):
        for j in range(len(B)):
            if A[i] == B[j]:
                break
        else:
            C.append(A[i])
    return C

def main():
    A = [20, 40, 70, 30, 10, 80, 50, 90, 60]
    B = [35, 45, 55, 60, 50, 40]
    print(array_excluded_elements(A, B))
    
main()