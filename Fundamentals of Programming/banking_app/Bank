class Bank:
    
        
    def __init__(self):
               
        self.database = []#This is a class attribute is initialized to an empty list
        
    #This method acts soley on the class attribute database to update the list of Account objects.
    #this function should capture up to 100 client accounts, each element is an account object with retrievable attributes initialized in the Account class.
    #if an element in the list is 'null' that object is added to the list.
    def addAccountToBank(self, acc_object):

        if len(self.database) < 100:
            self.database.append(acc_object)
        else:
            print("No more accounts available")
            return False

    def removeAccountFromBank(self, closing_object):
        
        closing_object == 'null'
        return 'null'

    def findAccount(self, accountNumber):
        for i in self.database:
            if i.Account_number  == accountNumber:
                return accountNumber
            else:
                return 'null'
            
    def addMonthlyInterest(self,Num_Account, interest_acc,percent):
        
        #should add an annual interest to all the accounts in the array
        Add_interest = 0
        Added_interest = (interest_acc * (percent/100)/12)
        interest_acc = Added_interest + interest_acc
                
        print("Deposited interest: " ,"$" , Added_interest,"into account number: ", Num_Account, "New Balance: $", interest_acc)
       