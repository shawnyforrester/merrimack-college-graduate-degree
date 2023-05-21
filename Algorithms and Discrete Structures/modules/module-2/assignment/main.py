# Write a program that reads the people.csv file and creates a stack of Person objects.
# The user should be prompted for an integer input from numbers 1-4 and the corresponding number is popped
# from the stack and the last object in the stack is printed to the console.

from person import Person
from create_csv import create_csv
from stack import Stack


def main():
    # Create the csv file
    create_csv()
    # Create a stack
    stack = Stack()
    with open("people.csv") as file:
        # Read the file line by line
        for line in file:
            # Split the line into a list of values
            values = line.split(",")
            # Create a Person object
            person = Person(values[0], values[1], values[2], values[3])
            # Add the Person object to the stack
            stack.push(person)
    # Prompt the user for a number between 1-4
    
    while not stack.is_empty():
        number = eval(input("Enter a number between 1 and 4: "))       
        while number < 1 or number > 4:
            print("Invalid input\n")
            number = eval(input("Enter a number between 1 and 4: "))
        # Pop the corresponding number of elements from the stack
        for i in range(number):
            stack.pop()
            i+=1
        # Print the last object in the stack
        print(stack.peek())
      
        
        
        
      
            
        
    
    
    


if __name__ == "__main__":
    main()