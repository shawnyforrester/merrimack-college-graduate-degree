# Define the function that returns circumference, area and volume.

def Circumference(r):
    return round(2.0 * 22/7 * float(r), 2)
def Area(r):
    return round(22/7* float(r)**2.0, 2)
def Volume(r):    
    return round((4.0 * 22/7 * float(r)**3)/3.0, 2)

	
# Prompt the user for a number: “Hello! Please enter the radius measurement or type 0 to leave the program: ”
def main():
  
    while True:  
        x = input("Hello! Please enter the radius measurement or type 0 to end the program: ")
        if float(x) > 0:

            print ("Your radius is: " , x, "Thank you!") 
                 
# Print circumference, area and volume.
	
            print ("The circumference of a circle with a radius of: ", x, "is", Circumference(x))
            
            print ("The area of a circle with a radius of: ", x, "is", Area(x))
            
            print ("The volume of a sphere with a radius of: ", x, "is", Volume(x))
            
                 
#Reject invalid numbers    
        if float(x) < 0:
            input("This number is invalid. Please enter another number: ")
            continue
#Program end        
        if float(x) == 0:
            print("Thank you goobye")
            break
              
if __name__ == "__main__":
    main()
        

                     
    
    
