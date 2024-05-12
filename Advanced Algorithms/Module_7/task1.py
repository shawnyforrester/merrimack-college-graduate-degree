"""Create a program that generates a random array of 10,000 elements with equal number of 0's and 1's and then implement the randomized Las Vegas algorithm that searches for an element holding a 1
Your program should output the position of the first 1 found, plus the number of tries before finding it"""

import numpy as np

#this method creates an array with 10,000 elements with equal number of 0's and 1's
def random_array():
    length = 10000
    half_length = length // 2    
    
    zeros = np.zeros(half_length, dtype=int)
    ones = np.ones(half_length, dtype=int)
    arr = np.concatenate((zeros, ones))
    np.random.shuffle(arr)  
    return arr     


def randomized_las_vegas(arr):
    count = 0
    while True:
        count += 1
        index = np.random.choice(len(arr), replace = False) #choice is used here to ensure that a number is not picked more than once
        if arr[index] == 1:
            break
        else: 
            continue   
    return index, count           
                

def main():
    arr = random_array()
    index, count = randomized_las_vegas(arr)
    print(f"Index: {index}, Number of tries: {count}")
    print(arr)
    
if __name__ == "__main__":
    main()  