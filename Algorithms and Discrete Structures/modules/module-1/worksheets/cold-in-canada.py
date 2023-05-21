# '''
# *Is it cold in Canada Today?*
# This program will ask the user for the current temperature in Fahrenheit 
# and the temperature threshold in Celsius. 
# It will then convert the threshold to Fahrenheit and 
# compare the two temperatures. 
# If the current temperature is greater than the threshold, 
# it will print "It is cold in Canada." Otherwise, 
# it will print "It is not cold in Canada."
#'''


def get_temperature():
    # Get the temperature threshold from the user
    cold_threshold = float(input("What is the temperature in Celsius? "))
    temp_F = (9/5) * float(cold_threshold) + 32
    
    #Get the current temperature from the user
    current_temp = float(input("What is the current temperature in Fahrenheit? "))
    
    # Compare the current temperature with the threshold and return the result
    if float(current_temp) > temp_F:
        print("It is cold in Canada.")
    else:
        print("It is not cold in Canada.")
        
    # Endfunction
    
def main():
    # Call the get_temperature function
    get_temperature() 
    

    
if __name__ == '__main__':
    main()
    
    