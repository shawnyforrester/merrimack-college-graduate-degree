"""Write a function that takes an integer n as input and creates a vector of length n.
The vector should contain the integers 1 through n in order. The function should then
swap the first two elements of the vector, the next two elements, and so on. The function
should print the vector after each swap. """
def swap(n, vec):    
    
    # Swap the elements
    for i in range(0, n-1, 2):
        vec[i], vec[i+1] = vec[i+1], vec[i]
        print("Vector after swap:", vec) 
    


def main():
    #Ask for user input
    n = eval(input("Please enter an integer: "))
    
   # Create the initial vector
    vec = list(range(1, n+1))
    print("Initial vector:", vec)
    swap(n, vec)
    
    
if __name__ == "__main__":
    main()
        
        