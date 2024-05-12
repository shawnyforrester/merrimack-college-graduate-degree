"""Write python code for a recursive algorithm that will calculate the number of digits in the
binary expansion/representation of a positive integer n. The logic of the recursive algorithm
should be something like:
if n = 1, the answer is 1;
if n > 1, the answer is 1 more than the number of digits in the binary representation of
n/2 """

def binary(n):
    if n == 1:
        return 1
    elif n > 1:
        return binary(n//2) + 1
    else:
        raise ValueError("Input must be a positive integer")


def main():
    integer = int(input("Enter a positive integer: "))
    print(f"Printed outcome:  {binary(integer)}")
    
if __name__ == "__main__":
    main()