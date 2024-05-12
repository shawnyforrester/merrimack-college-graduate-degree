"""Create a program that implements a sort algorithm of your choice and applies it to a random vector of 1,000 elements
Repeat the process applying it to random vectors of 2,000, 3,000, ... up to 10,000 elements
Compute the time complexity of your algorithm and verify if the time it takes to your 1,000 to 10,000 corresponds to the time complexity prediction."""

import cProfile
from contiguous_subsequence import array_generator, max_subsequence

    

def merge_sort(array):
    """Sorts an array using merge sort"""  
    if len(array) > 1:
        mid = len(array) // 2
        left = array[:mid]
        right = array[mid:]
        
        merge_sort(left)
        merge_sort(right)
        
        i = j = k = 0
        
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                array[k] = left[i]
                i += 1
            else:
                array[k] = right[j]
                j += 1
                
            k += 1
            
        while i < len(left):
            array[k] = left[i]
            i += 1
            k += 1
            
        while j < len(right):
            array[k] = right[j]
            j += 1
            k += 1
            
    return array

def main():
    """Main function"""
    array = array_generator()
    merge_sort(array)
    
if __name__ == "__main__":
    cProfile.run("main()")