"""Run the balanced01mat.py program and compute the number of balanced matrices for matrices of order 6 and 8 (run the program as it is to discover the numbers)
Change the program to instead of asking the user, calls it for 2, 4, 6, and 8 sequentially
Include remarks in the code with the expected values for 2, 4, 6, and 8"""

# balanced 0-1 matrices

from itertools import combinations

def permutations(n):
    ones = list(combinations(list(range(n)),n//2))
    ans = []
    for o in ones:
        case = []
        for i in range(n):
            if (i in o):
                case.append(1)
            else:
                case.append(0)
        ans.append(case)
    return ans

def check(mat):
    n = len(mat[0])
    for j in range(n):
        acc0, acc1 = 0, 0
        for i in range(len(mat)):
            if (mat[i][j] == 1):
                acc1 += 1
            elif (mat[i][j] == 0):
                acc0 += 1
            if (acc0 > (n//2)) or (acc1 > n//2):
                return False
    return True

def layer(r, mat, perm, ans):
    for p in perm:
        mat.append(p)
        if check(mat):
            if (r+1 == len(p)):
                ans += 1
            else:
                ans = layer(r+1, mat, perm, ans)
        mat.pop()
    return ans

#For a martix of n^2 number of outcomes the overall expected possible combinations for an unbalanced matrix of 1's and 0's
#is 2^(n^2).  

# For a balanced matrix the possible combinations are:
#When n = 2, is 2 out of a possible 16 combinations
#When n = 4, is 90 out of a possible 65,536 combinations
#When n = 6, is 297,200 out of a possible 69,719,476,736
#When n = 8, is 1.844674407371e19

def balanced01mat():
    print("Computing the number of balanced matrices")
    n = 1
    while ((n % 2) == 1) or (n < 0):
        n = int(input("Enter an even matrix order:"))
    perm = permutations(n)
    ans = layer(0, [], perm, 0)
    print("The number of balanced matrices is", ans)

balanced01mat()