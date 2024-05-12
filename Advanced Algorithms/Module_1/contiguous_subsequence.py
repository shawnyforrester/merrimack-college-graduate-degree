"""Create a program that randomizes a vector of 1000 positive and negative integers, 
then finds the maximum contiguous subsequence sum value
Prints out the maximum value"""

import random

def array_generator():
    """Generates an array of 1000 random integers between -100 and 100"""    
    array = []
    # for i in range(1000):
    # for i in range(2000):
    # for i in range(3000):
    # for i in range(4000):
    # for i in range(5000):
    # for i in range(6000):
    # for i in range(7000):
    # for i in range(8000):
    # for i in range(9000):        
    for i in range(10000):        
        
        array.append(random.randint(-100, 100))
    return array

"""Finds the maximum contiguous subsequence sum value"""
def max_subsequence(array):
    
    """A recursive function that finds the maximum contiguous subsequence sum value"""
    # #base case    
    # if (len(array)) == 1:
    #     return array[0]
    # #recursive case
    # else:
    #     i = 0
    #     largest_sum = array[0]
    #     current_sum = max_subsequence(array[i]) + max_subsequence(array[i:])
    #     if current_sum > largest_sum:
    #         largest_sum = current_sum
    #     i += 1
    # return largest_sum #returns the maximun value - task 1 and returns the indexes of the subsequence - task 2
    
    """A non-recursive function that finds the maximum contiguous subsequence sum value (O(n^2))"""   
    # largest_sum, current_sum = 0, 0    
    # for i in range(len(array)):
    #     for j in range(i, len(array)):
    #         current_sum = sum(array[i:j+1])
    #         if current_sum > largest_sum:
    #             largest_sum = current_sum                
    #             first_index = i
    #             last_index = j
    # return largest_sum, first_index, last_index #returns the maximun value - task 1 and returns the indexes of the subsequence - task 2

    """A non-recursive function that finds the maximum contiguous subsequence sum value (O(n))"""
    largest_sum, current_sum, i = 0, 0, 0
    for j in range(len(array)):
        current_sum += array[j]
        if current_sum > largest_sum:
            largest_sum = current_sum
            i = j + 1
        elif current_sum < 0:
            current_sum = 0
    return largest_sum, j, i #returns the maximun value - task 1 and returns the indexes of the subsequence - task 2

def main():
    """Main function"""
    # array = array_generator()
    array = [-2, 34, -16, 9, -32, 12, 38, -1, 81, -76, 9, 34, -4, 12]
    print(max_subsequence(array))
    
    
if __name__ == "__main__":
    main()