"""Write a recursive algorithm to determine the mean of the numbers in a non-empty array using
the strategy that is illustrated by the following two examples with an array of 5 numbers (notice
the recursive call with one less entry in the array) and an “array” of 1 number (think base case of
the recursive algorithm):
mean( {40, 50, 60, 70, 80}) = 4/5 ∗ mean( {40, 50, 60, 70}) + 1/5 ∗ 80
𝑚ean({40}) = 40
Your function should have two parameters – the array of numbers and an integer indicating how
many of the array values should be included in the calculations (note this is not the subscript of
the last element of the array) – and should return the calculated value of the mean using a return
statement.

For example, given five numbers stored in array A (in slots A[0]..A[4]), the function call
Mean(A, 5)
would cause a return of
4/5*Mean(A, 4) + 1/5*A[4].

Of course, the parameter in your code for the definition of the function would be n; the 4s and 5s
would not show up explicitly in the code.
b) Run your code on the problem instances:
i) A1 = <12, 23, 37, 45, 63, 82, 47, 75, 91, 88, 102> 11 entries
ii) A2 = <-1.7, 6.5, 8.2, 0.0, 4.7, 6.3, 9.5, 12.2, 37.9, 53.2> 10 entries
"""

def array_mean(array, n):
    if n == 1:
        return array[0]
    else:
        return (n-1)/n*array_mean(array, n-1) + 1/n*array[n-1]
    
def main():
    print(array_mean([12, 23, 37, 45, 63, 82, 47, 75, 91, 88, 102], 11))
    print(array_mean([-1.7, 6.5, 8.2, 0.0, 4.7, 6.3, 9.5, 12.2, 37.9, 53.2], 10))
    
if __name__ == "__main__":
    main()