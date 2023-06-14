"""Write Python code for the bubble sort algorithm to sort an array into ascending order, but
with the possibility of an early exit if there are no swaps on some iteration through the outer
loop. Modify the code in the class notes to do four things:

i) On each iteration through the outer loop, count the number of times two array elements
are compared and the number of times two array elements are swapped. Reinitialize these
counters to zero at the beginning of each iteration.
ii) After each iteration through the outer loop, print three things: the partially sorted array,
the number of comparisons on this iteration, and the number of swaps on this iteration.
After the kth iteration, you should see that at least the k largest elements have “bubbled
up” into the last k slots of the array.
iii) If there are no swaps on some iteration through the outer loop, the array is now sorted,
so terminate the algorithm.
iv) When the algorithm concludes (after n-1 iterations or after an early exit), display the
total number of comparisons of array elements and the total number of swaps required to
sort the array.
b) Check your algorithm on the problem instances:
A4 = [44, 63, 77, 17, 20, 99, 84, 6, 39, 52]
A5 = [52, 84, 6, 39, 20, 77, 17, 99, 44, 63]
A6 = [6, 17, 20, 39, 44, 52, 63, 77, 84, 99]
"""

    
def BubbleSort(A):
    """Sorts array A into ascending order."""
    n = len(A)
    swap_count = 0
    compare_count = 0
    for k in range(n - 1):
        # Find the index of the largest element in A[i...n-1]
        print("Iteration Number:", k + 1, "\nArray:", A)
        swaps_made = False
        for j in range(n - 1 - k):
            if A[j + 1] < A[j]:
                compare_count += 1
                print("Compare Count:", compare_count,
                      "(", "Comparing", A[j], "and", A[j + 1], ")")
                # Swap the elements at indices j and j+1
                swap_count += 1
                A[j], A[j + 1] = A[j + 1], A[j]
                swaps_made = True
                print("Swap Count:", swap_count, "(", "Swapping", A[j], "and", A[j + 1], ")")
        if not swaps_made:
            print("No swaps on this iteration, so the array is sorted.")
            break
    print("Total Compare Count:", compare_count, "\nTotal Swap Count:", swap_count)

#main function    
def main():
    A = [52, 84, 6, 39, 20, 77, 17, 99, 44, 63]
    BubbleSort(A)
    print("Sorted array:", A)
    
if __name__ == "__main__":
    main()