import csv

#This function creates a csv file and writes the data to it
def create_csv():
    # Create a list of data as a list of lists
    data = [
        [35, 2, 3, 3, 0],
        [40, 2, 2, 2, 1],
        [45, 3, 2, 5, 2],
        [58, 2, 3, 4, 3]
    ]
    
    # Create a csv file and write the data to it
    with open("packs.csv", "w", newline='') as file:
        writer = csv.writer(file)      
        
        # Write the data rows
        writer.writerows(data)


