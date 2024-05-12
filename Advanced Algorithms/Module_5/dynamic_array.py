from random import randrange

def test(initialSize, probRemove):
    accCheap, accCostly = 0, 0
    s = initialSize
    m = 2*s
    for i in range(100000):
        if (randrange(100) < probRemove):
            if (s > 0):
                s -= 1
        else:
            if (s == m):
                m = m*2
                s += 1
                accCostly += 1
            else:
                s += 1
                accCheap += 1
    print("Initial size:", initialSize, "Prob Remove:", probRemove, "out of 100")
    print("Costly: {:7} ({:3.1}%)".format(accCostly,accCostly/(accCostly+accCheap)))
    print("Cheap: {:7} ({:3.1}%)".format(accCheap,accCheap/(accCostly+accCheap)))

def main():
    
    test(1, 67) #This test gives .000009% probability of costly operations
    test(20, 44) #This test gives a .0002% probability of costly operations
    test(18, 36) #This test also gives a .0002% probability of costly operations
    # test(10, 1)
    # test(10, 5)
    # test(20, 1)
    # test(20, 5)
    # test(50, 1)
    # test(50, 5)
    # test(100, 1)
    #test(100, 5)

main()

# Comments: It appears that the probability of costly operations is direclty proportional to the initial size of the array.
#This is because a smaller array will have to resize more often, and thus will have more costly operations.
#The probability of costly operations is also directly proportional to the probability of removing an element.
#It is our random number generator that really determines whether or not an operation is costly or cheap.
#As such, the outcome of costly operations is also influenced by the random number generator.
