"""Implement a Double Array Queue and test it for a very large case (100,000 randomly decided operations of enqueue or dequeue)
Your program should compute the number of costly operations and cheap operations
Your program should also ask the user about the ratio between enqueue and dequeue operations:
The probability of enqueues and dequeues should never be of less than half the other (34% enqueues - 66% dequeues or 66% enqueues - 34% dequeues)"""

import random

class Queue:
    def __init__(self):
        self.a_in = [None]
        self.a_out = [None]

    def enqueue(self, d):
        return self.a_in.append(d)

    def dequeue(self):
        if self.a_out == []:
            for d in self.a_in:
                self.a_out.append(d)
            self.a_in = []
        return self.a_out.pop(0)

def main():
    #instantiate the double array queue
    q = Queue()
    costly, cheap = 0, 0
    #Request the user to enter the enqueue/dequeue ratio
    while True:
        eqRatio = float(input("Please enter an EQ (enqueue/dequeue ratio not less than 0.5 or enter 0 to end the program: "))  
        if eqRatio == 0:
            exit()
        elif eqRatio < 0.5:
            print("Please enter a ratio not less than 0.5")
            continue
        else:
            break  
    #Request the user to enter the initial size of the double array
    try:
        size = int(input("Please enter the initial size of the array: "))
    except ValueError:
        print("Please enter a valid integer")
        exit()
    #set the initial size of the double array
    q.a_in, q.a_out = [None] * size, [None] * size
    m = 2*size
    #Perform 100,000 random operations of enqueue and dequeue
    for i in range(100000):
        if random.random() < eqRatio :
            q.enqueue(i)
            if size == m:
                m = m*2
                size += 1
                costly += 1
            else:
                size += 1
                cheap += 1          
        else:
            q.dequeue()
            s =-1
    print("Initial size:", size, "EQ Ratio:", eqRatio, "out of 100")
    print("Costly: {:7} ({:3.1}%)".format(costly,costly/(costly+cheap)))
    print("Cheap: {:7} ({:3.1}%)".format(cheap,cheap/(costly+cheap)))

if __name__ == "__main__":
    main()


    