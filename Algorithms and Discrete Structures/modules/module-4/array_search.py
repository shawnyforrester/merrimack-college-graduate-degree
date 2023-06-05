"""Find the number of entries in an array of integers that are divisible by a given integer. 
Your function should have two input parameters – an array of integers and a positive integer – 
and should return an integer indicating the count using a return statement"""

#this method counts the number of items in an array that are divisible by a given divisor
def count_divisible_items(arr, divisor):
    count = 0
    for i in arr:
        if i % divisor == 0:
            count += 1
    return count

def main():
    #prompt user for input
    array = []
    run = True
    while run:
        element = int(input("Enter a number from 1-10 (to end type 0): "))
        array.append(element) #add element to array
        if element == 0:
            run =False #break out of loop if user enters 0     
    
    while True:
        divisor = int(input("Enter a positive integer: "))#prompts the user for a positive integer
        if divisor > 0:
            break        
    #prints the number of items in the array that are divisible by the given divisor
    print("The number of items in the array that are divisible by", divisor, "is", count_divisible_items(array, divisor))
    
if __name__ == "__main__":
    main()