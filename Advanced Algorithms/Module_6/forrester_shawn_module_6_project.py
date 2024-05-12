"""Implement a Linear Pogramming model to solve the following problem:
Your program shoudl recevie the necessary information for an LP problem namely:
The number of variables ( That will be equal to the number of constraint coeeficients), x , The coeffieicnt of each variable for the ibjective  function, f(x)
The data for the square matrix stating the constraint coefficients, A and the right hand side of the constraints, b, the constraint limits
Having all input parameters, your program should solve the LP problem and print the optimal solution and the optimal value of the objective function.
Use the nump package and the functions, array, linalg.inv and linalg.solve to solve the problem."""
import numpy as np


def function(variables, constA, constb):
    A = np.array(constA)
    inv_A = np.linalg.inv(A)
    b = np.array(constb)
    print("This is the optimal solution for this problem",
          variables, " = ", np.linalg.inv(A).dot(b))


def main():

    variables = []
    constA = []
    constb = []
    stay = True
    while stay:  # add an exit option
        try:
            x = eval(
                input("How many variables are there? To exit please enter 0: "))
            if x < 0:
                print("Invalid input, try again")
                continue
            if x == 0:
                print("Exiting...")
                exit()
        except (ValueError, SyntaxError):
            print("Invalid input, try again")
            continue
        for i in range(x):
            variable = input("Enter the variable: ")
            variables.append(variable)
        # request user input for constraints A

        try:
            constraint_number = eval(
                input("Please enter the number of expressions or press 0 to exit: "))
            if x < 0:
                print("Invalid input, try again")
                continue
            if x == 0:
                print("Exiting...")
                exit()

        except (ValueError, SyntaxError):
            print("Invalid input, try again")
            continue
        for i in range(constraint_number):
            constraint = eval(
                input("Enter the constraints separated by a comms: "))
            constA.append(constraint)

            # request user input for constraints b
        try:
            constraint_limits = eval(
                input("Please enter the number of constraint limits or enter 0 to exit: "))
            if x < 0:
                print("Invalid input, try again")
                continue
            if x == 0:
                print("Exiting...")
                exit()
        except (ValueError, SyntaxError):
            print("Invalid input, try again")
            continue
        for i in range(constraint_limits):
            limit = eval(input("Enter the constraint limit: "))
            constb.append(limit)
        print(function(variables, constA, constb))
        stay = (
            "n" != (input("\nCompute another? (no to stop) ").lower() + " ")[0])


if __name__ == "__main__":
    main()

# Test Case 1 for pizza and sandwiches x and y respectively, the user is prompted to enter the number of variables, the number of constraints, the constraints, and the constraint limits:
# How many variables are there? To exit please enter 0: 2
# Enter the variable: x
# Enter the variable: y
# Please enter the number of expressions or press 0 to exit: 2
# Enter the constraints separated by a comms: 8,3
# Enter the constraints separated by a comms: 1,1
# Please enter the number of constraint limits or enter 0 to exit: 2
# Enter the constraint limit: 60
# Enter the constraint limit: 10
# This is the optimal solution for this problem ['x', 'y']  =  [6. 4.]
# None


# Teset Case 2 for pants and jackets x and y respectively, the user is prompted to enter the number of variables, the number of constraints, the constraints, and the constraint limits:
# How many variables are there? To exit please enter 0: 2
# Enter the variable: x
# Enter the variable: y
# Please enter the number of expressions or press 0 to exit: 2
# Enter the constraints separated by a comms: 2,3
# Enter the constraints separated by a comms: 2,1
# Please enter the number of constraint limits or enter 0 to exit: 2
# Enter the constraint limit: 1500
# Enter the constraint limit: 1000
# This is the optimal solution for this problem ['x', 'y']  =  [375. 250.]


# Test case 3 for the Chemical Factory:
# How many variables are there? To exit please enter 0: 3
# Enter the variable: x
# Enter the variable: y
# Enter the variable: z
# Please enter the number of expressions or press 0 to exit: 3
# Enter the constraints separated by a comms: 2,4,5
# Enter the constraints separated by a comms: 1,2,4
# Enter the constraints separated by a comms: 8,0,3
# Please enter the number of constraint limits or enter 0 to exit: 3
# Enter the constraint limit: 300
# Enter the constraint limit: 200
# Enter the constraint limit: 300
# This is the optimal solution for this problem ['x', 'y', 'z']  =  [25.         20.83333333 33.33333333]
