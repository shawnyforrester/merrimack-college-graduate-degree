"""In his famous math book Elements, Euclid included an algorithm (that he might or might not
have invented) to find the GCD of two positive integers. The basic idea is as follows:

For example, GCD (144, 42) = GCD (42, 18) = GCD (18, 6) = GCD (6, 0) = 6

a) Code this algorithm in Python. Use the appropriate Python operator to implement the modular
arithmetic operation.

Your function should have two parameters – the two integer whose GCD is being determined –
and should return the calculated value of the GCD using a return statement.
Before each recursive call, have your algorithm print out the two integers that were passed in as
parameters. Have the driver/main program print out the result of the initial function call (that is,
the final result).
b) Run your code on the problem instances:
i) GCD (2468, 1357)
ii) GCD (111, 378)
iii) GCD (123456789, 987654321)
"""

def euclidean_algorithm(a, b):
    if b == 0:
        return a
    else:
        print(a, b)
        return euclidean_algorithm(b, a % b)
    
def main():
    print("*********** Euclidean Algorithm ***********")
    print("****GCD (2468, 1357)****")
    print(euclidean_algorithm(2468, 1357))
    print("****GCD (111, 378)****")
    print(euclidean_algorithm(111, 378))
    print("****GCD (123456789, 987654321)****")
    print(euclidean_algorithm(123456789, 987654321))
    
if __name__ == "__main__":
    main()