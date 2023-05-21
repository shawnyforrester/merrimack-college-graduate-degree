import csv
from person import Person

def create_csv():
    with open('people.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        field = ['firstname', 'lastname','age', 'occupation']
        
        writer.writerow(field)
        writer.writerow(['John', 'Anderson', '45', 'Plumber'])
        writer.writerow(['Jane', 'Bafter', '43', 'Electrician'])
        writer.writerow(['Jack', 'Baker', '23', 'Teacher'])
        writer.writerow(['Jill', 'Baker', '25', 'Artist'])        
        writer.writerow(['Usian', 'Bolt', '27', 'Athlete'])
        writer.writerow(['James', 'Bond', '37', 'MI6'])
        writer.writerow(['Sean', 'Connory', '37', 'Exterminator'])
        writer.writerow(['Sara', 'Connor', '27', 'CIA'])
        writer.writerow(['Robert', 'Downey', '47', 'IronMan'])
        writer.writerow(['Michael', 'Drake', '27', 'Rapper'])
        writer.writerow(['Farah', 'Faucet', '29', 'Detective'])
        writer.writerow(['Barak', 'Obama', '42', 'President'])
        writer.writerow(['Zack', 'Morris', '27', 'School Administrator'])
        writer.writerow(['Sean', 'Stevens', '27', 'Artist'])
        writer.writerow(['William', 'Thomas', '31', 'Writer'])
        writer.writerow(['Benny', 'Tzcak', '56', 'Scientist'])
        
        
        