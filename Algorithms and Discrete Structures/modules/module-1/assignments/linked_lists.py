"""
Create a program that reads a list of Integer numbers from a file named data.txt (create your own file with about 16 numbers - no repetitions and one number per line)
Store those numbers into an array a and sort it - a.sort()
Use the linked list and node classes seen in class to store the ordered elements of a into a LinkedList structure L
Ask the user a Integer value x
Look for the position to insert x in L
If the value x is already in L, remove it
If it is not, insert x in the appropriated position so L remains sorted
Go to IDLE and try to program it
Save your program in a .py file and submit 

Efficency of LinkedList operations:
    Insertion: O(1)
    Deletion: O(1)
    Search: O(n)
    Access: O(n)

"""


"""
This class defines the node structure with a data field and a next field"""


class Node:

    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.previous = None


"""This class defines the linked list structure with a head field or head node"""


class LinkedList:

    # class constructor
    def __init__(self):
        self.head = None
        self.tail = None

    # print function to print the linked list
    def print_list(self):
        print_val = self.head
        while print_val is not None:
            print("'", print_val.data, "'" + " -> ", end="")
            print_val = print_val.next

    # method to insert a new node at the beginning of the linked list
    def add_value(self, new_data):
        new_node = Node(new_data)
        new_node.previous = self.tail

        if self.tail == None:  # checks if the list is empty
            self.head = new_node
            self.tail = new_node
            new_node.next = None

        else:
            self.tail.next = new_node
            new_node.next = None
            self.tail = new_node

    # this is a method to determine the length of the list

    def length(self):
        current_node = self.head
        total = 0

        while current_node.next is not None:
            total += 1
            current_node = current_node.next
        return total
    
     

    # this method inserts a value at a node in the listed maintaining the sorted order
    def insert_sorted_no_duplicates(self, value):
        new_node = Node(value)
              
        if self.head is None:
            self.head = new_node
        elif self.head.data == value:
            new_node.next = self.head.next
            new_node.previous = self.head.previous
            self.head = new_node
        
        else:
            current = self.head
            while(current.next is not None and current.data !=value):
                current = current.next            
                
            if current.next is None:
                current.next = new_node
                new_node.previous = current
                new_node.next = None
                                 
            if current.data == value:
                current.next.previous = current.previous
                current.previous.next = current.next
                current = None    
                
            
                 
                

"""This is the main function which will read the data.text file and store each line in an array which will then be sorted and stored in a singly linked 
linked list structure L"""


def main():

    number_array = []
    L = LinkedList()
    

    # read the data.txt file and store each line in an array
    with open("data.txt", 'r') as f:
        for line in f:
            number_array.append(int(line))

    # sort the array
        number_array.sort()
    # insert the sorted array into the linked list L
        for integer in number_array:
            L.add_value(integer)
    # print the sorted linked list
    L.print_list()

    # ask the user for a number to insert into the linked list
    list_entry = True
    while list_entry is True:
        x = eval(input("\nPlease enter a number to insert into the linked list or enter 0 to end: "))
        if x == 0:
            list_entry = False
            break
        L.insert_sorted_no_duplicates(x)
        L.print_list()


if __name__ == "__main__":
    main()


