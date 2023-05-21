


#define a function  that asks for 2 positive intgers.
def func():
    int_1 = eval(input("Please enter the first of two numbers: "))
    if int_1 >= 0:
        int_2 = eval(input("Thank you! Please enter another number: "))
        if int_2 >= 0:
            while not ((int_1 % int_2) == 0 or (int_2 % int_1) == 0):
                return False
            
            #returns True if either evenly divides the other
            if ((int_1 % int_2) == 0 or (int_2 % int_1)) == 0:
                return True
            
#Calling function which displays the boolen.           
def print_boolean():  
    
    #Program ends once the correct numbers are obtained.
    if (func()) is True:      
        print("Evenly divisible! Thank you!")

     
    #Loop keeps asking for divisible numbers.
    while (func()) is False:
        print("Not evenly divisible! Please try again!")
               
print_boolean()
        

    

    


        


            
    


            
            

        



            






    

    

    
        
    
        




