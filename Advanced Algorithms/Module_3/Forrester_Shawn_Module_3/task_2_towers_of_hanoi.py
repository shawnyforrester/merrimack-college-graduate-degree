"""Implement a recursive program that asks the
number of disks and delivers the minimal number
of moves to solve the Towers of Hanoi efficiently.
Your program must have a recursive function that
delivers the number of movements for a given
number of disks"""

# This recrusive function is based on the recursive formula 2f(n - 1) + 1 which gives the number of moves for n disks


def hanoi(n):
    # n =1 represents our base case
    if n == 1:
        return 1
    return 2 * hanoi(n-1) + 1

# This main function prompts the user for n, the number of disks, and then calls the hanoi function to calculate the number of moves


def main():
    while True:
        try:
            number = int(input("Please enter the number of disks: "))
            break
        except ValueError:
            print("Please enter a valid integer.")

    print("The number of moves is", hanoi(number))


if __name__ == "__main__":
    main()
