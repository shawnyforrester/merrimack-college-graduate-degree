"""Create a program that receives the list of possible named items with the following information:

Value ($), Height (in), Width (in), Depth (in)

The limit of the optimal solution is expressed by the volume in cubic inches (in^3) and the program has to maximize the value within the cubic limit
Your program should read a textual file with one item type per line with the information separated by comma, for example this fileLinks to an external site. lists four items with values 35, 40, 45, and 58 dollars and increasing dimensions
Your program should capture the overall limit of the package/knapsack from the user.
Your program should read any file with this format (name, value, height, width, depth) per line
Your program must print out the best distribution with a string like: "The suggested items are: 72 Milky Ways and 5 Tootsie Rolls with a total value of $53. There were 4 square inches left unused."
The printed statement must at least include: names of items included; number of items included; total profit; leftover space."""

import csv
from create_csv import create_csv

#function that takes the list of items and the capacity of the knapsack and returns the optimal solution
def knapsack(packs, capacity):    
    collection = []
    total_value = 0
    total_cbin = 0
    output = set() #using a set to store unique elements   

    #iterate through the list of items and calculate the rate of value per volume 
    for item in packs:
       item_value, item_width, item_height, item_depth, item_id = item
       item_volume = item_width * item_height * item_depth
       collection.append([item_value/item_volume, item_value, item_volume, item_id])
       collection.sort(reverse=True) #sort from high to low rate
    
    #iterate through the sorted collection and add items to the knapsack (output)
    for item in collection:
         item_rate, item_value, item_volume, item_id = item
         if item_volume <= capacity:
           capacity -= item_volume
           total_value += item_value
           total_cbin += item_volume
           output.add(item_id)  
    remaining_cbin = capacity     
    return list(output),total_value, remaining_cbin


#main function that reads the file and calls the knapsack function
def main(): 
    item_names = ['Blue Sparkles', 'Perfect Pinks', 'Gigantic Greens', 'Orange Oblongs']
    #create a csv file and write the data to it
    create_csv()
    #create a list of lists with the data
    packs = []
    pack = []
    #open and read the file
    data = open("packs.csv", "r")
    for line in data:
        line = line.rstrip("\n")
        pack.append(int(x) for x in line.split(","))
    for i in pack:
        packs.append(i)
    data.close()

    #prompt the user for a capacity
    while True:        
        capacity = int(input("Enter the capacity of the knapsack or enter 0 to end the program: "))
        if capacity == 0:
            print("Goodbye!")
            exit()
        elif capacity < 0:
            print("Invalid input. Please try again.")
            continue
        else:
            break
    
    #call the knapsack function    
    output, total_value, remaining_cbin = knapsack(packs, capacity)
    
    # Count the occurrences of items in the output
    count = {}
    for item_id in output:
        count[item_id] = count.get(item_id,0) + 1

    print("The suggested items are:")
    for item_id, count in count.items():
        print(f"{count} x Item {item_names[item_id]}")

    print(f"With a total value of {total_value}")
    print(f"There were {remaining_cbin} cubed inches left unused.")

if __name__ == "__main__":
    main()