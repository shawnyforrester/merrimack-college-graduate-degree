#Import functions random and time to facilitate the random list generation and function execution time respectively
import random
import time


#This function generates a list of random numbers ensuring that no elements are repeated
#This main function also calls both sort functions and generates the time to execution for each
def main():
    data = []
    sampleSize = 20
    final_list = 0
    
    while final_list < sampleSize:
        r = random.randint(0, 100)
        if r not in data:
            data.append(r)
            final_list +=1
        

    print(data)
    start_time_merge = time.time()
    print(merge_sort(data))
    print('Merge sort execution time: {}'.format(start_time_merge - time.time()))

    start_time_bubble = time.time()
    print(bubblesort(data))
    print('Bubble sort execution time: {}'.format(start_time_bubble - time.time()))



#This merge sort function splits the sample list in two halves. The elements in each half are searched linearly as both sublists get smaller and smaller in the number of elements - hence
# quasilinear time complexity. A shorter exection time is expected.


def merge_sort(data):
   
    if len(data) <= 1:
        return
    
    mid = len(data) // 2
    left_data = data[:mid]
    right_data = data[mid:]
    
    merge_sort(left_data)
    merge_sort(right_data)
    
    left_index = 0
    right_index = 0
    data_index = 0
    
    while left_index < len(left_data) and right_index < len(right_data):
        if left_data[left_index] < right_data[right_index]:
            data[data_index] = left_data[left_index]
            left_index += 1
        else:
            data[data_index] = right_data[right_index]
            right_index += 1
        data_index += 1
    
    if left_index < len(left_data):
        del data[data_index:]
        data += left_data[left_index:]
        
    elif right_index < len(right_data):
        del data[data_index:]
        data += right_data[right_index:]
  
    return data 

#This bubble sort function performs linear operations on every element in the list without creating sublists. Once a condition is met adjacent elements are swapped until no further swaps are made.
#As such this function has a higher level of time complexity a longer execution time is expected.
def bubblesort(data):

    start_time = time.time()
    
    swapped = False
    while not swapped:
        swapped = True
        for i in range (len(data) -1):
            if data [i] > data[i + 1]:
                data[i], data[i + 1] = data [i +1], data[i]
    
    return data


if __name__ == '__main__':
    main()
