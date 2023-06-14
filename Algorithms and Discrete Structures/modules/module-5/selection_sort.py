"""Write Python code for the selection sort algorithm to sort an array into ascending order, but
modify the code in the class notes to do three things:

i) After k iterations through the outer loop, the k LARGEST elements should be sorted
rather than the k SMALLEST elements.
ii) On each iteration through the outer loop, count the number of times two array
elements are compared and the number of times two array elements are swapped.
Reinitialize these counters to zero at the beginning of each iteration.
iii) After each iteration through the outer loop, print three things: the partially sorted
array, the number of comparisons on this iteration, and the number of swaps on this
iteration. After the kth iteration, you should see that the k largest elements have been
placed into the last k slots of the array.
b) Check your algorithm on the problem instances:
A1 = [63, 44, 17, 77, 20, 6, 99, 84, 52, 39]
A2 = [84, 52, 39, 6, 20, 17, 77, 99, 63, 44]
A3 = [99, 84, 77, 63, 52, 44, 39, 20, 17, 6]
"""


def Swap(A, i, j, swap_count):
    """Swaps the elements at indices i and j of array A."""
    temp = A[i]
    A[i] = A[j]
    A[j] = temp
    print("Swap Count: ", swap_count, "(", "Swapping", A[i], "and", A[j], ")")


def SelectionSort(A):
    """ Sorts array A into ascending order."""
    n = len(A)
    iteration = 0
    swap_count = 0
    compare_count = 0
    for k in range(n-1, 0, -1):
        iteration += 1
        # Find the index of the largest element in A[i...n-1]
        print("Iteration Number: ", iteration, "\n", "Array:", A)
        biggerIndex = k
        for j in range(k-1, -1, -1):
            if A[j] > A[biggerIndex]:
                compare_count += 1
                print("Compare Count: ", compare_count,
                      "(", "Comparing", A[j], "and", A[biggerIndex], ")")
                biggerIndex = j
                swap_count += 1
        # Swap the elements at indices k and biggerIndex
        if biggerIndex != k:
            Swap(A, k, biggerIndex, swap_count)


def main():
    """Tests the selection sort algorithm."""
    A = [84, 52, 39, 6, 20, 17, 77, 99, 63, 44]
    SelectionSort(A)
    print("Sorted array:", A)


if __name__ == "__main__":
    main()
