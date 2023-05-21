"""Zigzag problem

Create a function zigzag that gets three values as input parameters
let's call them a, b, and c.
The function should return True if a < b > c or 
a > b < c and False otherwise.
"""
#Main function
def main():
    zigzag(1, 2, 3)
    
    
#This function determines if a, b, and c are in zigzag order
def zigzag(a, b, c):
    if (a < b > c) or (a > b < c):
        return True
    else:
        return False
#End function zigzag

if __name__ == "__main__":
    main()