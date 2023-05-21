class Account:

    def __init__(self, Account_number, first_nam, Last_nam, SSN, PIN, Balance):
        #These attributes are initialized everytime this class is instantiated.
        self.Account_number = Account_number
        self.first_nam = first_nam
        self.Last_nam = Last_nam
        self.SSN = SSN
        self.PIN = PIN
        self.Balance = Balance
        
        
    def setPIN(self, Pin_set, Customer_acc):#This function takes two parameters, the new PIN and the customer account(An Account object) and then sets the PiN
        #on the account.
        Customer_acc.PIN == Pin_set
        return True
        
    def toString(self):
        #returns a string that contains the names and values of all the attributes
        print(f"Account Number: {self.Account_number}\n", f"Owner's First Name: {self.first_nam}\n", f"Owner's Last Name: {self.Last_nam}\n",
              f"Owner's SSN: {self.SSN}\n", f"PIN: {self.PIN}\n", f"Balance: {self.Balance}\n")
        
        
    def deposit(self, add_sum, deposit_acc_bal):#An attribute deposit_object(An Account object) was added
        #so that the correct account balance could returned.
        deposit_acc_bal == deposit_acc_bal + add_sum
        return deposit_acc_bal

    def withdraw(self, withdrawal_amt, withdrawal_acc_bal):# An attribute withdrawal_object was added
        #so that the corrent balance could be returned.
       if withdrawal_acc_bal < withdrawal_amt:
           print("Insufficient Funds")
       else:
           withdrawal_acc_bal == withdrawal_acc_bal - withdrawal_amt
           return withdrawal_acc_bal
        
        
        
##   def isValidPIN(self, pin): #This function checks for a valid PIN
##        self.pin = pin