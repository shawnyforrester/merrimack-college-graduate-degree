"""Task 1: Create a program that randomizes an array of
1000 integers from 1 to 1,000,000 and verify the
uniqueness of its elements using the brute force
algorithm"""

import random

#This function produces the random array
def random_array():
    array = []
    for i in range(1000):
        array.append(random.randint(1,1000000))
    return array

#In this main function we check if the array is unique
def main(): 
    array = random_array()
    status = "This array is unique"  
    
    #Algorithm no. 1 checks if the array is unique, Big O(n) time complexity  
    # for i in array:
    #     if array.count(i) > 1:
    #         status = "This array is not unique"            
    #         break
    # print(status)
    
    #Algorith no.2 checks if the array is unique, Big O(n^2) time complexity
    for i in array:
        for j in array:
            if i == j and array.index(i) != array.index(j):
                status = "This array is not unique"
                break
    print(status)       
        

if __name__ == "__main__":
    main()    

        
  