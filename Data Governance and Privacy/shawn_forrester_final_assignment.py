import pandas as pd
import numpy as np
from hashlib import sha256


# Function to replace letters after hyphen with asterisk
def replace_letters_after_hyphen(text):
    parts = text.split('-')  # Split the text by hyphens
    if len(parts) > 1:
        parts[1:] = ['*' * len(part) for part in parts[1:]]  # Replace each part after the first hyphen with asterisks
    return '-'.join(parts)  # Join the parts with hyphens and return the result

def categorize_age(age):
    if age < 30:
        return '20-29'
    elif age < 40 and age >= 30:
        return '30-39'
    elif age < 50 and age >= 40:
        return '40-49'
    else :
        return '50-59'
    
def risk_calculator(count):
    if count == 0:
        return 0
    else:
        return 1/count
    
    

# Main function
def main():
    xlsx_file = 'Merr.xlsx'
    # Read the XLSX file
    data = pd.read_excel(xlsx_file) 
    
    # print(data)     
    
    data['Age Group']= [categorize_age(age) for age in data['Age']]    
       
    #Counts the number of 1s in Gender column that are in a given Age Group 20-29
    count_ones_20 = data[(data['Age'] >= 20) & (data['Age'] < 30)][data['Gender']== 1] ['Gender'].sum()
    #Counts the number of 1s in Gender column that are in a given Age Group 30-39
    count_ones_30 = data[(data['Age'] >= 30) & (data['Age'] < 40)][data['Gender']== 1] ['Gender'].sum()
    #Counts the number of 1s in Gender column that are in a given Age Group 40-49
    count_ones_40 = data[(data['Age'] >= 40) & (data['Age'] < 50)][data['Gender']== 1] ['Gender'].sum()
    #Counts the number of 1s in Gender column that are in a given Age Group 40-49
    count_ones_50 = data[(data['Age'] >= 50) & (data['Age']< 60)][data['Gender']== 1] ['Gender'].sum()
    
    #Calculate the number of 0s in Gender column that are in a given Age Group 20-29
    count_zeros_20 = len(data[(data['Age'] >= 20) & (data['Age'] < 30)]) - count_ones_20
    #Counts the number of 1s in Gender column that are in a given Age Group 30-39
    count_zeros_30 = len(data[(data['Age'] >= 30) & (data['Age'] < 40)]) - count_ones_30
    #Counts the number of 1s in Gender column that are in a given Age Group 40-49
    count_zeros_40 = len(data[(data['Age'] >= 40) & (data['Age'] < 50)]) - count_ones_40
    #Counts the number of 1s in Gender column that are in a given Age Group 40-49
    count_zeros_50 = len(data[(data['Age'] >= 50) & (data['Age']< 60)]) - count_ones_50   
     
    gender_categories= [count_ones_20, count_ones_30, count_ones_40, count_ones_50, count_zeros_20, count_zeros_30, count_zeros_40, count_zeros_50]

   
           
    #Create a new dataframe with the new columns    
    new_data = pd.DataFrame ({
        "Age Group": ["20-29", "30-39", "40-49", "50-59", "20-29", "30-39", "40-49", "50-59"],
        "Gender Categories": [1,1,1,1,0,0,0,0],
        "Risk Probability": [risk_calculator(count) for count in gender_categories]
    })
    
    output_file = 'filtered_data.xlsx'
    
    # Write the new dataframe to an XLSX file
    new_data.to_excel(output_file, index=False)   

    
    
if __name__ == '__main__':
    main()



