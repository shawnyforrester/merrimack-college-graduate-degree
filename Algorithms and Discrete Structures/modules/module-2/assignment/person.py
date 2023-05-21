"""This program creates a list of people from a the people.csv file
The objects are stored in a stack. 
The user is prompted for an integer input from numbers 1-4 and the corresponding number is popped
from the stack and the last object in the stack is printed to the console.
"""


class Person:
    """Person class that stores the name, age, and occupation of a person"""

    def __init__(self, firstname, lastname, age, occupation):
        """Constructor for the Person class"""
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.occupation = occupation
        
    # Getters and setter methods
        
    def get_firstname(self):
        return self.firstname 
    
    def get_lastname(self):
        return self.lastname
    
    def get_age(self):
        return self.age
    
    def get_occupation(self):
        return self.occupation
    
    def set_firstname(self, firstname):
        self.firstname = firstname
        
    def set_lastname(self, lastname):
        self.lastname = lastname
    
    def set_age(self, age):
        self.age = age
    
    def set_occupation(self, occupation):
        self.occupation = occupation

    def __str__(self):
        """Returns a string representation of the Person object"""
        return f"{self.firstname} {self.lastname} is {self.age} years old and works as a {self.occupation}"
       
