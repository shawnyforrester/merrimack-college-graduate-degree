"""Randomized algorithm to find an element in an array Write a Python function alea() that creates and returns a randomized array of 1000 
elements that may have its elements with one of three possible values: 2, 3, or 4 with roughly the same probability to each value. 
Write a Python pick(a) function that receives the randomized vector created by the function alea() 
and looks for any element of a with the value 2, and prints the element's index in the array. 
However, this function pick(a) has to use a randomized algorithm that has O(1)"""
 
import random

def alea():    
    a = []
    for i in range(1000):
        a.append(random.randint(2,4))
    return a

def pick(a):    
    while True:
        i = random.randint(0,999)
        if a[i] == 2:
            return i

def main():
    a = alea()
    print(len(a))
    print(pick(a))

main()
        
