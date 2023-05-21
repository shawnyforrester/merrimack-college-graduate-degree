class Deque:

    def __init__(self):
        self.Baby_Shower_List = []
 
       
    def Add_Left(self, item):
        self.item = item
        self.Baby_Shower_List.insert(0, self.item)
        return self.Baby_Shower_List
      
    def Add_Right(self, item):
        self.item = item
        self.Baby_Shower_List.append(self.item)
        return self.Baby_Shower_List
    
    def Remove_item(self, wrong_item):
        self.Baby_Shower_List.remove(wrong_item)
        return
         
    def Display_List(self):
        
        print("Your list is: ", self.Baby_Shower_List)
        

def main():

    deque = Deque()
    
    n = eval(input("How many Baby Shower items will you need?: "))
    Order = input("Will you be entering the least important first or last?: ")
    
    while Order.upper() != "FIRST" or Order.upper() != "LAST":
        update_order = input("Please confirm 'first' or 'last': ")
        if update_order.upper() == "FIRST" or update_order.upper() == "LAST":
            break
                
                
    i = 0  
    while i <= n:
        i = i + 1
        
        List_item = input("Please enter your Baby Shower item: " )
                
        if Order.upper() == "LAST":
            deque.Add_Right(List_item)
            
                     
                   
        if Order.upper() == "FIRST":
            deque.Add_Left(List_item)
            
          
    deque.Display_List()
        
    no_item = input("Too many items! Would you like to remove an item? ")
    if no_item.upper() == "YES":
        remove_item = input("Please state the item: ")
        deque.Remove_item(remove_item)
        deque.Display_List()
        
    else:
        print("Thank you")
        
        
        
if __name__ == '__main__':
    main()
