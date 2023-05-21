
class Rectangle:
   
    def __init__(self, width, length):
        
        '''The __init__ method initializes the class attributes.'''
        self.width = width  
        self.length = length
        
    def Perimeter(self):
        '''Perimeter method is defined to return the perimeter of the rectangle'''
        return  (self.width * 2) + (self.length * 2)
        
    def Area(self):
        '''Area method is defined to return the area of a rectangle'''
        return self.width * self.length 
        
    
    def display(self):
        '''The print function is defined to display the width and length given in each instance of the class Rectangle and then prints the area and perimeter passed from the Perimeter and Area methods respectively''' 
        
        print(f"The perimeter of your Rectanagle width = {self.width} and length = {self.length} is {self.width * 2 + self.length * 2}")
        print(f"The Area of your Rectangle width = {self.width} and length = {self.length} is {self.width * self.length }")
        
class Parallelepiped (Rectangle):
    
           
    def __init__(self, h, width, length):
        '''The child class Parallelepiped inherits attributes from the parent class, h, the height, is specified attribute for this class'''
        super().__init__(width, length)
        self.h = h
          
    def Volume(self):
        '''Volume is the method created in this class to return the volume of the 3-d object'''
        return self.width * self.length * self.h
    
print(Parallelepiped.__init__.__doc__)    
print(Parallelepiped.Volume.__doc__)        
print(Rectangle.Area.__doc__)
print(Rectangle.Perimeter.__doc__)
print(Rectangle.__init__.__doc__)
print(Rectangle.display.__doc__)

def main():

    '''This function prompts the user to input values for the width and length, ensuring that only valid numbers are passed to the predefined class attributes'''    
    width = eval(input("Please enter the width of your rectangle or type 0 to exit: " ))
    while width < 0 == True:
        print("Invalid entry! Please try again")
    if width == 0:
        exit()
    
    print(f"Thank you! The width is {width}")     
    length = eval(input("Please enter the length of your rectangle: "))
    while length < 0 == True:
        print("Invlaid entry! Please try again")
        
    '''Here the display method is called. The returned value is printed'''  
    rec = Rectangle(width, length)
    print(rec.display())
    
    '''Here the user is prompted to put in a value for height which is then passed to the h attribute in the predefined Parallelepiped class method above'''
    height = eval(input("Please enter the height of the Parallelepiped: "))
    while height < 0 == True:
        print("Invalid entry! Please try again")

    P = Parallelepiped(width, length, height)
    print(f"Thank you! The height is {height}")
    print("Your volume is", P.Volume())


print(main.__doc__)

if __name__ == '__main__':
    main()



