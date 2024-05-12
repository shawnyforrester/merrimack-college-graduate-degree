"""Write python code for a recursive algorithm that will calculate the sum of the squares of the
positive integers 1^2 + 2^2 + 3^2 + ... + 𝑛^2 when supplied with a positive integer n.
The logic of the recursive algorithm should be something like:
if n = 1, the answer is 1;
if n > 1, the answer is (the sum of the squares of the integers from 1 to n-1) + 𝑛^2."""

def sum_of_squares(n):
    if n == 1:
        return 1
    elif n > 1:
        return sum_of_squares(n-1) + n**2
    else:
        raise ValueError("Input must be a positive integer")

def main():
    integer = int(input("Enter a positive integer: "))
    print(f"Printed outcome:  {sum_of_squares(integer)}")
    
if __name__ == "__main__":
    main()