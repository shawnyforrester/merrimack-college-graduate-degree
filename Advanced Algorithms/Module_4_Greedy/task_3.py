# knapsack unbounded - Greedy approach

def knapsack(v, w, cap):
    rwv = []         # triplet ratio, weight, value, index
    for i in range(len(v)):
        rwv.append([v[i]/w[i],w[i],v[i],i])
    rwv.sort(reverse=True)    # sort from high to low rate
    ans = []                     # the list of added items
    tw = 0                                  # total weight
    found = True
    while (found):        # until no fitting item is found
        found = False
        for t in rwv:              # search an item to add
            if (t[1] + tw) <= cap:      # if the item fits
                ans.append(t[3])                  # add it
                tw += t[1]
                found = True
                break
    return ans           # returns the list of added items

def main():
    items = int(input("Number of distinct items: "))
    values, weights = [],[]
    for i in range(items):
        v = int(input("Value of item "+str(i+1)+": "))
        w = int(input("Weight of item "+str(i+1)+": "))
        values.append(v)
        weights.append(w)
    capacity = int(input("Maximum weight (capacity): "))
    answer = knapsack(values, weights, capacity)
    tv, tw = 0, 0
    for a in answer:
        print("Item - Value:", values[a], "- Weight:", weights[a])
        tv += values[a]
        tw += weights[a]
    print("Items:", len(answer), "- Value:", tv, "- Weight:", tw)

if __name__ == "__main__":
    main()


# Test Case 1 Input: ([5,10] [8,20] [12,30]) - capacity 838    Output:Items: 83 - Value: 415 - Weight: 830
# Test Case 2 Input: ([3,17] [5,23] [7,29] [11,31] [13,37] - capacity 997    Output:Items: Items: 32 - Value: 352 - Weight: 992
# Test Case 3 Input: ([5,25] [6,36] [7,49] [8,64]) - capacity 250    Output:Items: Items: 10 - Value: 50 - Weight: 250
# Test Case 4 Input: ([5,25] [6,36] [7,49] [8,64]) - capacity 360    Output:Items: Items: 14 - Value: 70 - Weight: 350
