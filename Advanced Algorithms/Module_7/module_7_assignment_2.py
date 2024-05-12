"""Create a program that calls the function myFunction(x) from 0 to 9999 and applies the Hill Climbing algorithm to find the value of x that delivers the largest value for the function
Implement a version where the initial search value x is chosen randomly between the values 1 to 9998
You can use this function to test your program, but your program should work with any version of myFunction(x)"""


from math import log2
import random
import time


def myFunction(x):
    if (x == 0):
        return 0
    elif ((log2(x) * 7) % 17) < (x % 13):
        return (x + log2(x)) **3
    elif ((log2(x) * 5) % 23) < (x % 19):
        return (log2(x) + log2(x)) **3
    else:
        return int(abs((log2(x)**2) - x))

#Hill climb algorithm
def hillClimb(arr, start_index): 
      
    
    while start_index >= 0 and start_index <= len(arr)-1:
        
        if start_index == 0:
            if arr[start_index] > arr[start_index + 1]:
                local_maximum_index = start_index
                break
            else:
                start_index += 1
                continue
        elif start_index == len(arr)-1:
            if arr[start_index] > arr[start_index - 1]:
                local_maximum_index = start_index
                break
            else:
                start_index -= 1
                continue
        elif arr[start_index + 1] > arr[start_index]:
            start_index += 1
            
        elif arr[start_index - 1] > arr[start_index]:
            start_index -= 1
            
        elif arr[start_index - 1] < arr[start_index] and arr[start_index + 1] < arr[start_index]: 
            local_maximum_index = start_index
            break
        elif arr[start_index - 1] ==  arr[start_index]:
            start_index -= 1
            continue
        elif arr[start_index + 1] == arr[start_index]:
            start_index += 1
            continue         
    
    return local_maximum_index, arr[local_maximum_index]

#This main function generates an array calling myFunction from 0 to 9999 and then calls the Hill climb function 
def main():
    arr = []
    index = random.randint(0,10000) #randomly samples a number between 0 and 9999
    for i in range(10000):
    # index = random.randint(0,10) #randomly samples a number between 0 and 9999
    # for i in range(10):
        arr.append(myFunction(i))
        random.shuffle(arr) #the shuffle method was included to add randomness to the array creating the peaks and troughs for the hill climb algorithm
        
    print(f"This is the array: {arr} and the random index: {index}\n") 
    print("Loading Hill Climb Algorithm...\n")   
    time.sleep(3)
    print(f"This is the local maximum index and it's value respectively: {hillClimb(arr, index)}")

if __name__ == "__main__":
    main()