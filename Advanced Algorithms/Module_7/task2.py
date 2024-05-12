"""Create a program that generates a random array of 10,000 elements with equal number of 0's and 1's and then implement the randomized Monte Carlo algorithm that searches for an element holding a 1
○Set k equal to 10
○Your program should output the position of the first 1 found, plus the number of tries before finding it or a message stating that it did not find the 1 after k attempts."""

import numpy as np

#this method creates an array with 10,000 elements with equal number of 0's and 1's
def random_array():
    length = 10000
    half_length = length // 2    
    
    zeros = np.zeros(length, dtype=int)
    ones = np.ones(half_length, dtype=int)
    arr = np.concatenate((zeros, ones))
    np.random.shuffle(arr)  
    return arr

#this method implements the randomized Monte Carlo algorithm that searches for an element holding a 1
def monte_carlo(arr, k):
    count = 0
    while count < k:
        count += 1
        index = np.random.choice(len(arr), replace = False) #choice is used here to ensure that a number is not picked more than once
        if arr[index] == 1:
            return index, count
    return None, count

#main method that calls the functions and prints the outcomes.
def main():
    
    while True:
        try:
            k = int(input("Please enter a number greater than 0 or enter 0 to cancel: "))
            if k == 0:
                exit()
            elif k < 0:
                continue
            else:
                break
        except:
            ValueError
            continue
        
    arr = random_array()
    index, count = monte_carlo(arr,k)
    if index:
        print(f"Index: {index}, Number of tries: {count}")
    else:
        print(f"Sorry no 1s found after {count} attempts")
    
if __name__ == "__main__":
    main()
    