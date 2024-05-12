"""Create a program that computes the "Tribonacci" sequence numbers
Unlike the traditional Fibonacci sequence (a number is the sum of the two previous ones), here a number is the sum of the three previous ones (the initial numbers are 1,1,1)

The first 9 elements of the sequence are:
1, 1, 1, 3, 5, 9, 17, 31, 57, …

Your program should asks the user a positive Integer n and the deliver the n-th element of the Tribonacci sequence"""

# This recursive algorithm gives the nth element of the Tribonacci sequence
# def tribonacci(n):
#     if n == 1 or n == 2 or n == 3:
#         return 1
#     return tribonacci(n-1) + tribonacci(n-2) + tribonacci(n-3)


# This is a dynamic programming algorithm that gives the nth element of the Tribonacci sequence
def tribonacci(n):
    # the first three elements of the Tribonacci sequence are 1, 1, 1
    sequence_list = [1, 1, 1]
    # if n is less than or equal to 3, then the nth element of the Tribonacci sequence is 1
    if n <= 3:
        return 1
    # if n is greater than 3, then we use a for loop to calculate the nth element of the Tribonacci sequence

    for i in range(3, n):
        # the ith element of the Tribonacci sequence is the sum of the previous three elements
        sequence_list.append(sequence_list[i-1] +
                             sequence_list[i-2] + sequence_list[i-3])
    return sequence_list[-1]

# This is the main function that prompts the user for n, the nth element of the Tribonacci sequence, and then calls the tribonacci function to calculate the nth element


def main():
    while True:
        try:
            number = int(
                input("Please enter a positive integer or exit the program by entering 0: "))
            if number == 0:
                print("Exiting program...")
                break
            # the nth element of the Tribonacci sequence is printed here
            print(tribonacci(number))
            continue
        except ValueError:
            print("Please enter a valid integer or exit the program by entering 0")


if __name__ == "__main__":
    main()
