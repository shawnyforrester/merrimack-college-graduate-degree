"""Create a program that randomizes an array of
1000 integers from 1 to 1,000,000 and verify the
uniqueness of its elements using the transform-and-conquer algorithm"""
import random


#This function produces the random array
def random_array():
    array = []
    for i in range(1000):
        array.append(random.randint(1,1000000))
    return array

#This function sorts the array
def merge_sort(array):
    if len(array) > 1:
        mid = len(array)//2
        left = array[:mid]
        right = array[mid:]
        
        merge_sort(left)
        merge_sort(right)
        
        i = j = k = 0
        
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                array[k] = left[i]
                i+=1
            else:
                array[k] = right[j]
                j+=1
            k+=1
        
        while i < len(left):
            array[k] = left[i]
            i+=1
            k+=1
        
        while j < len(right):
            array[k] = right[j]
            j+=1
            k+=1
    return array

#Here the the sorted array is checked for duplicates. Big O (n log n) time complexity
def main():
    array = random_array()
    array = merge_sort(array)
    status = "This array is unique"
    for i in range(len(array)-1):
        if array[i] == array[i+1]:
            status = "This array is not unique"
            break
    print(status)
    
if __name__ == "__main__":
    main()