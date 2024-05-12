#task 1

# Egyptian fraction Greedy
from math import ceil
  
# n is the numerator, d is the denominator
def egyptian(n, d):
  
    print("The Egyptian Fraction of {}/{}".format(n, d))
    ans = []
    output = []
    # while numerator is not 0
    while (n > 0):
        x = ceil(d / n)          # compute the minimal larger denominator
        ans.append(x)            # hold it to the numerator list
        n, d = x * n - d, d * x  # update the remainder to n and d
    for a in ans:
        output.append("1/{}".format(a))
    print(",".join(output))        
        # print("1/{}".format(a), end=" ")


def main():
    print("Greedy Algorithm to Compute Egytian Fractions")
    stay = True
    while stay:
        n = int(input("Enter the numerator: "))
        d = int(input("Enter the denominator: "))
        egyptian(n, d)
        stay = ("n" != (input("\nCompute another? (no to stop) ")+" ")[0])

main()

#Case solutions:
# 5/6 = 1/2 + 1/3
# 7/15 = 1/3 + 1/8 + 1/120
# 23/34 = 1/2 + 1/6 + 1/102
# 121/321 = 1/3 + 1/1538 + 1/4729350
# 5/123 = 1/25 + 1/1538 + 1/4729350