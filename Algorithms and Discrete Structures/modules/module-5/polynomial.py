"""Write a Python function
power (x, p)
to calculate the value of 𝑥^𝑝 for any real number x and any non-negative integer p.
The brute-force function should use a for loop to repeatedly multiply the value of x.
Do not use Python’s exponentiation operator ** to evaluate x**p"""

def power_function(x, p):  
    result = 1
    if p == 0:
        return 1
    elif x == 0:
        return 0
    elif p > 0 and x > 0:                          
        for i in range(p):
            result *= x
        return result
    else:
        print("Error: Invalid input. Please enter a real number x and a non-negative integer p.")

"""Write a Python function
evaluate (A, x)
that determines the value of f(x) for the polynomial that is represented by the corresponding
array A of coefficients. For each term of the polynomial, this function should make a call to the
power() function that you wrote in part3a.
c) Run your code to evaluate the polynomial
𝑓(𝑥) = 12.3 + 40.7𝑥 − 9.1𝑥^2 + 7.7𝑥^3 + 6.4𝑥^4 + 8.9𝑥^6
at x = 5.4
"""
def polynomial_function(A, x):
    function_degree = len(A) -1
    result = 0
    for i, coefficient in enumerate(A):
        value = coefficient * power_function(x, function_degree - i)
        result += value
    return round(result, 2)          

#main function        
def main():
    x = float(input("Enter a real number x: "))
    p = int(input("Enter a non-negative integer p: "))
    print("x^p =", power_function(x, p))    
   
if __name__ == "__main__":
    main()