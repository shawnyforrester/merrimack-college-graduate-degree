"""Given an integer n>=2 and two nxn matrices A and B of real numbers, find the product AB of the matrices.
Your function should have three input parameters – a positive integer n and two nxn matrices of numbers– and should return the nxn product matrix using a return statement."""

def nxn_product_matrix(n, A, B):
    """Return the nxn product matrix of two nxn matrices A and B."""
    # Create an empty nxn matrix to store the product matrix.
    product_matrix = [[0 for i in range(n)] for j in range(n)]
    # Iterate through rows of A.
    for i in range(n):
        # Iterate through columns of B.
        for j in range(n):
            # Iterate through rows of B.
            for k in range(n):
                # Multiply the elements of A and B and add them to the product matrix.
                product_matrix[i][j] += A[i][k] * B[k][j]
    # Return the product matrix.
    return product_matrix

def main():
    #Initialize the matrices A and B.
    A = []
    B = []
    # Prompt the user to enter a positive integer.
    while True:
        try:            
            n = int(input("Enter a positive integer: "))
            # Check if the integer is positive.
            if n > 0:
                break
            # Raise a ValueError if the integer is not positive.
            else:
                raise ValueError
        except ValueError:
            print("Invalid input. Please try again.")
    # Prompt the user to enter the elements of the first matrix.
    for i in range(n):
        row = []
        for j in range(n):
            element = float(input(f"Enter the element at row ({i}, {j}): "))
            row.append(element)
        A.append(row)
    # Prompt the user to enter the elements of the second matrix.
    print("Enter the elements of the second matrix: ")
    for i in range(n):
        row = []
        for j in range(n):
            element = float(input(f"Enter the element at row ({i}, {j}): "))
            row.append(element)
        B.append(row)

    # Print the product matrix.
    print("The product matrix = ", nxn_product_matrix(n, A, B))    
            
    
    
    
if __name__ == "__main__":
    main()