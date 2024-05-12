"""Create a function that receives an array of
numbers, sort this array and return the mode"""
import random

#Gets the random array O(n) complexity
def random_array():
    array = []
    for i in range(1000):
        array.append(random.randint(1,1000000))
    return array



#Gets the mode of the array O(n log n) complexity
def main():
    
    array = random_array()  
    
    array.sort() #sorts the list in ascending order with O(n log n) complexity  
    mode = array[0] 
    count , maxCount = 0, 0, 
    
    for i in range(len(array)-1):
        if array[i] == array[i+1]:
            count+=1
        else:
            if count > maxCount:
                maxCount = count
                mode = array[i]            
    print(mode)
    
if __name__ == "__main__":
    main()