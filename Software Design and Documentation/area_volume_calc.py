
""" This module contains a class that can be used to calculate the area and volume of 
a circle given the radius of the circle. 

Attributes: 
radius (float): The radius of the circle."""

class Circle:
    
    """ Initialize the Circle object with the radius of the circle.
    Args: 
    radius(float): The radius of the circle."""
    def __init__(self, radius):
        self.radius = radius

    """Calculate the circumference of the circle.
    Returns: 
    float: The circumference of the circle."""
    def circumference(self):
        return 2 * 3.14159 * self.radius
    
    """Calculates the area of the circle.
    Returns: 
    float: The area of the circle."""

    def area(self):
        return 3.14159 * self.radius ** 2
    """Calculates the volume of the sphere.
    Returns: 
    float: The volume of the sphere."""
    def volume(self):
        return 4/3 * 3.14159 * self.radius ** 3
    
    
    
def main():
    radius = 5
    c = Circle(radius)
    print("The circumference of the circle is: ", c.circumference())
        
if __name__ == "__main__":
        main()
        
        
        
    

    


        

                     
    
    
