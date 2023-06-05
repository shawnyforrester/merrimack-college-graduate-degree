"""Given an array of real numbers, without sorting the array, 
find the smallest gap between all pairs of elements (for an array A, 
the absolute value of the difference between elements 𝐴[i] and 𝐴[𝑗]). 
Your function should have one input parameter – an array of numbers – 
and should return a non-negative number indicating the smallest gap 
using a return statement"""

def smallest_gap(arr):
    smallest_gap = abs(arr[0] - arr[1])
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if abs(arr[i] - arr[j]) < smallest_gap:
                smallest_gap = abs(arr[i] - arr[j])
    return smallest_gap

def main():
    #prompt user for input
    array = []    
    length = int(input("Enter the length of the array: "))
    if length > 0:
        for i in range(length):
            element = float(input("Enter a number: "))
            array.append(element)#add element to array           
    #prints the smallest gap between all pairs of elements in the array
    print("The smallest gap between all pairs of elements in the array is", smallest_gap(array))
    
if __name__ == "__main__":
    main()