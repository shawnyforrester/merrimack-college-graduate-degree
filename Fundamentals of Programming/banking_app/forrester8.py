import random

#Creating accounts -a list of Account objects        
Bank_accounts =[] #An array of Account objects representing client data            
Account_PIN_Log = []#An array of Bank objects representing account data

class Account(object):
    
    def __init__(self, Account_Number, First_Nam, Last_Nam, SSN, PIN, Bal):
        self.Account_Number = Account_Number
        self.First_Nam = First_Nam
        self.Last_Nam = Last_Nam
        self.SSN = SSN
        self.PIN = PIN
        self.Bal = Bal  
      
    def getBalance(self, accountnum):
        self.accountfrom = accountfrom
        if i.Account_Number == accountnum:
            return i.Bal
     
    #Used for selection 2, to retrieve the Account attributes in the Bank_accounts database and then prints them.    
    def getAccountInfo(self, getPIN, getAccount_Number):
        self.getPIN = getPIN
        self.getAccount_Number = getAccount_Number
        
        for i in Bank_accounts:
            if i.Account_Number == getAccount_Number:
                i.toString()
                
    def updateAccount(self, number):
        self.number = number
        for Client in Bank_clients:
            if Client.Account_Number == number:
                return False
            else:
                Client.Account_Number == number

    def update_PIN(self, acc_num, PIN_num):
        self.PIN_num = PIN_num
        selfacc_num = acc_num
        for i in Bank_accounts:
            if i.Account_Number == acc_num:
                i.PIN == PIN_num
                return True
    
    # add methods as getters and setters for attributes
    #Wrtite 2 unittests for EACH - deposit, withdraw and isValidPIN
    
    
    def Update_BAL_deposit(self, acc_num, deposit_amt):
        self.acc_num = acc_num
        self.deposit_amt = deposit_amt

        for i in Bank_accounts:
            if i.Account_Number == acc_num:
                i.Bal = i.Bal + deposit_amt
                return i.Bal
     
        
    #This method withdraws a specified amount from     
    def withdraw(self, client_acc, amount):
        self.amount = amount
        self.client_acc = client_acc

        for i in Bank_accounts:
            if i.Account_Number == client_acc:
                if i.Bal > self.amount:
                    i.Bal = i.Bal - self.amount
                    return i.Bal
                else:
                    return 'Insufficient Funds'
    
    
    def isValidPIN(self, pin):#May not be needed to check for a valid PIN, to work in the main function an instance of the Account class mnust be created.
        self.pin = pin
        for i in Bank_accounts:
            if i.PIN == self.pin:
                return True
            else:  
                return False  
    
    
    # all objects have a toString method - this indicates you are providing
    # your own version
    
    def toString(self):
        #returns a string that contains the names and values of all the attributes
        print(f"Account Number: {self.Account_Number}", "\n", f"Owner's First Name: {self.First_Nam}\n", f"Owner's Last Name: {self.Last_Nam}\n",
              f"Owner's SSN: {self.SSN}\n", f"PIN: {self.PIN}\n", f"Balance: {self.Bal}\n")
    
##    def __rep__(self):
##
##        return "" # change this as needed
    
class Bank(Account):
        
#At least 2 test units must be written for EACH method!
    def __init__(self):
        super(). __init__ (Account_Number, First_Nam, Last_Nam, SSN, PIN, Bal) 
        
        
        
    def addAccountToBank(self, Acc_NUM):
        self.Acc_NUM = Acc_NUM
        
        for i in Account_PIN_Log:
            if Account_PIN_log[i] == None:
                Account_PIN_log
                return True
            else:
                print("No more accounts available")
                return False; 

    def removeAccountFromBank(self, account_no):
        for i in Account_PIN_Log:
            if i.Account_Number == account_no:
                i.Account_Number == 'null'
                return 'Account closed'
        
    
    def findAccount(self, accountNumber):
        self.accountNumber = accountNumber
        
        for i in Account_PIN_Log:
            if i  == self.accountNumber:
                return accountNumber
            else:
                return 'null'    

    def addMonthlyInterest(self,interest_acc,percent):
        #should add an annual interest to all the accounts in the array
        self.percent = percent
        self.interest_acc = interest_acc
        
        for client_account in Bank_accounts:
            if client_account.Account_Number == interest_acc:
                Added_interest = self.Bal * (percent/100)/12
                self.Bal = Added_interest + self.Bal
                print("Deposited interest: " ,"$" , Added_interest,"into account number: ", self.interest_acc, "New Balance: $", client_account.Bal)
       
        

def main():

    
    User_Selection = eval(input("""What do you want to do?\n\n
    1. Open an account\n
    2. Get account information and balance\n
    3. Change PIN\n
    4. Deposit money in account\n
    5. Transfer money between accounts\n
    6. Withdraw money from account\n
    7. ATM withdrawal\n
    8. Deposit change\n
    9. Close an account\n
    10. Add monthly interest to all accounts\n
    11. End Program\n"""))
  
    if isinstance(User_Selection, int):
        if User_Selection < 11:
            if User_Selection == 1:
                print("OPEN ACCOUNT\n")
                First_Nam = input("\t Enter Account Owner's First Name: \n")
                Last_Nam = input("\tEnter Account Owner's Last Name: \n")
                SSN = input("\tEnter Account Owner's SSN: \n")
                Account_Number = random.choices((0,9),k =8)
                PIN = random.choices((0,9), k=4)
                Bal = 0.00

                #An instance of an Account object is created here.
                client_account = Account(Account_Number, First_Nam, Last_Nam, SSN, PIN, Bal )
                #An instance of a Bank object is created here.                
                Account_PIN = Bank()
                #The Account object list is populated here.
                Bank_accounts.append(client_account)
                #The Bank object list is populated here.
                Account_PIN_Log.append(Account_PIN)
                
                client_account.toString()
            
                #This option gets account information and balance.
            elif User_Selection == 2:
                User_Acc_Number = input("Enter Account Number: \n")
                for Account_PIN in Account_PIN_Log:
                    while Account_PIN.a != User_Selection:
                        User_Acc_Number = input("Account Number not found!\n Please enter an existing account number: ")
                    User_PIN_2 = input("Enter PIN: \n")
                    for Account_PIN in Account_PIN_Log:
                        while Account_PIN.p != User_PIN_2:
                            User_PIN_2 = input("Invalid PIN!\n Please re-enter your PIN")                   
                
                        client_account.getAccountInfo(User_PIN_2, User_Acc_Number)
                        main()
                        
             #This method changes the PIN on someone's account, the isValidPIn method is called here using an Account instance.
            elif User_Selection == 3:
                User_Acc_Number_3 = input("Enter Account Number: \n")
                for Account_PIN in Account_PIN_Log:
                    while Account_PIN.a != User_Acc_Number_3:
                        User_Acc_Number_3 = input("Account Number not found!\n Please enter an existing account number: ")
                    
                    while Account_PIN.isValidPIN(User_PIN_3) is False:
                        User_PIN_3 = input("Enter PIN: \n")
                    #User is prompted to enter a new PIN    
                    New_PIN = input("Enter new PIN: \n")
                    while len(list(New_PIN)) < 4 and isdigit(NEW_Pin) is False:
                        New_PIN = input("PIN must be 4 digits \n Enter new PIN: \n")    
                    Confirm_PIN = input("Confirm new PIN: \n")
                    while New_PIN != Confirm_PIN:
                        Confirm_PIN = input("PINs did not match \n Confirm new PIN: \n")
                    client_account.update_PIN(User_Acc_Number_3,Confirm_PIN)
                    print("PIN updated\n Thank you!")

              #Deposit funds and update account balance
            elif User_Selection == 4:
                Account_number_4 = input("Enter Account Number: \n")
                while Account_PIN.a != Account_number_4:
                    Account_number_4 = input("Account Number not found!\n Please enter an existing account number: ")
                    
                    
                User_PIN_4 = input("Enter PIN: \n")
                while Account_PIN.isValidPIN(User_PIN_4) is False:
                    User_PIN_4 = input("Account Number not found!\n Please enter an existing account number:")

                Deposit = eval(input("Please enter the amount for deposit  eg 2.57:  \n"))
                while Deposit < 0:
                    Deposit = eval(input("Amount cannot be negative!\n Please enter the amount for deposit eg 2.57: \n"))
              
                print("New Balance: ${}".format(client_account.Update_BAL_deposit(Account_number_4,Deposit)))
                main()        

             #Transfer money between accounts.
            elif User_Selection == 5:
                Account_from_Number_5 = input("Account to Transfer from: \n Enter Account Number: \n")
                while Account_PIN.a != Account_number_5:
                    Account_number_4 = input("Account Number not found!\n Please enter an existing account number: ")
                PIN_from_5 = input("Enter PIN: \n")
                while client_account.isValidPIN(PIN_from_5) is False:
                    PIN_from_5 = input("Invalid PIN!\n Please re-enter your PIN")
                       
                Account_to_Number_5 = input("Account to Transfer to: \n Enter Account Number: \n")
                while Account_PIN.a != Account_to_Number_5:
                    Account_to_number_5 = input("Account Number not found!\n Please enter an existing account number: ")

                PIN_to_5 = input("Enter PIN: \n")
                while client_account.isValidPIN(PIN_to_5) is False:
                    PIN_from_5 = input("Invalid PIN!\n Please re-enter your PIN")

                Transfer = eval(input("Enter amount to transfer in dollars and cents e.g. 2.57: \n"))
                print("New Balance in Account ", Account_from_Number_5, ":{}".format(client_account.withdraw(Account_from_Number_5,Transfer)),"\n",
                              "New Balance in Account ", Account_to_Number_5, ": {}".format(client_account.Update_BAL_deposit(Account_to_Number_5,Transfer)))
                main()

             #Account withdrawal, will need to set a new balance using a setter function 
            elif User_Selection == 6:
                Account_number_6 = input("Enter Account Number: \n")
                while Account_PIN.a != Account_number_6:
                    Account_number_6 = input("Account Number not found!\n Please enter an existing account number: ")

                PIN_6 = input("Enter PIN: \n")
                while client_account.isValidPIN(PIN_6) is False:
                    PIN_6 = input("Invalid PIN!\n Please re-enter your PIN")

                Withdraw = eval(input("Please enter the amount for Withdrawl: \n"))
                while Deposit < 0:
                    Deposit = eval(input("Amount cannot be negative!\n Please enter the amount for withdrawal eg 2.57: \n"))
              
                print("New Balance: ${}".format(client_account.withdraw(Withdraw)))
                main()

            #ATM cash withdrawal
            elif User_Selection == 7:
                Account_number_7 = input("Enter Account Number: \n")
                while Account_PIN.a != Account_number_7:
                    Account_number_7 = input("Account Number not found!\n Please enter an existing account number: ")
                    
                PIN_7 = input("Enter PIN: \n")
                while client_account.isValidPIN(PIN_7) is False:
                    PIN_7 = input("Invalid PIN!\n Please re-enter your PIN")
                  
                ATM_Withdraw = eval(input("Please enter the amount to withdraw in dollars (no cents) in multiples of $5 (limit $1000): \n"))
                while ATM_Withdraw < 0:
                    ATM_Withdraw = eval(input("Amount cannot be negative!\n Please enter the amount for withdrawal eg 2.57: \n"))

                ATM_Withdraw_ = BankUtility()
                if (client_account.getBalance(ATM_Withdraw)) > ATM_Withdraw:
                    ATM_Withdraw_.ATM_CASH(ATM_Withdraw)
                    print("New Balance: ${}".format(client_account.withdraw(Account_number_7, ATM_Withdraw)))
                    main()

            #ATM coin deposit 
            elif User_Selection == 8:
                    
                Account_number_8 = input("Enter Account Number: \n")
                while Account_PIN.a != Account_number_8:
                    Account_number_8 = input("Account Number not found!\n Please enter an existing account number: ")

                PIN_8 = input("Enter PIN: \n")
                while client_account.isValidPIN(PIN_8) is False:
                    PIN_8 = input("Invalid PIN!\n Please re-enter your PIN")
                        
                Coin_Deposit = CoinCollector()
                cents  = Coin_Deposit.parseChange(coins)
                coins = input("Deposit coins: ")
                print("$", Coin_Deposit.parseChange(coins), "in coins deposited into account")
                print("New Balance: {}".format(client_account.Update_BAL_deposit(Account_number_8, cents)))#prints an updated balance AFTER coin deposit
                main()

             #This prompt closes an account and sets the account for each client to none. Consider making Bank a child class of Account and using the setter function
            #the function should return 'Account xxxxx closed'
            # attempting to find the account should give an error message 'Account not found for account number: XXXX'    
            elif User_Selection == 9:
                Account_number_9 = input("Enter Account Number: \n")
                while Account_PIN.a != Account_number_9:
                    Account_number_9 = input("Account Number not found!\n Please enter an existing account number: ")
                    
                PIN_9 = input("Enter PIN: \n")
                while client_account.isValidPIN(PIN_9) is False:
                    PIN_9 = input("Invalid PIN!\n Please re-enter your PIN")

                print(Account_PIN.removeAccountFromBank(Account_number_9))#This is a Bank method called without an instance of a Bank class
            
            elif User_Selection == 10:
                #This selection should prompt the user to enter an annual interest rate and then find the client's balance and then add a monthly deposit based on the annual interest rate selected.
                    
                Account_number_10 = input("Enter Account Number: \n")
                while Account_PIN.a != Account_number_10:
                    Account_number_10 = input("Account Number not found!\n Please enter an existing account number: ")
        
                PIN_10 = input("Enter PIN: \n")
                while client_account.isValidPIN(PIN_10) is False:
                    PIN_10 = input("Invalid PIN!\n Please re-enter your PIN")

                Annual_Interest_Rate = eval(input("Enter annual interest rate percentage: "))
                Account_PIN.addMonthlyInterest(Account_numner_10, Annual_Interest_Rate)
                    
                main()
                    

                    
                
        elif User_Selection == 11:
            print("Thank you! Goodbye")
            exit
            
        else:
            print("Invalid choice\n")
            main()

        




    

##class BankManager(Bank):
##    
##    def __init__(self):
##        # This is where you will implement your ‘main’ method and start
##        # the program from.  The BankManager class should create an instance
##        # of a Bank object when the program runs and use that instance to
##        # manage the Accounts in the bank
##        self

           
       

                


      
##   def promptForAccountNumberAndPIN(self, #this_should be a bank_object):
##        
##        # implement promptForAccountNumberAndPIN here
##        # takes one parameter, a Bank object that represents the bank.
##        # The method should prompt the user to enter an account number
##        # and then try to find a matching account with that account number
##        # in the bank.
##
##        
##        Account_num = input("Please enter your 8 digit account number: \n")
##        if Account_num in Bank_data:
##            PIN = input("Please enter your 4 digit PIN: \n")
##                if PIN in Bank_data[Account_num]:
##                    return 
##                else:
##                    print("Invalid PIN")
##                    return 
##        else:
##            print("Account not found for account number: {}".format(Account_num))
##        return 









class BankUtility:
    #At least 2 unit tests shoudl be written for EACH function
    def __init__(self, cash_withdrawal):
        self. cash_withdrawal = cash_withdrawal
        

    def ATM_CASH(self, cash_withdrawal):
        
        self.cash_withdrawal = cash_withdrawal
        print("Number of 20-dollar bills: ", cash_withdrawal//20, "\n",
              "Number of 10-dollar bills: ", (cash_withdrawal%20)//10, "\n",
              "Number of 5-dollar bills: ", ((cash_withdrawal%20)%10)//5, "\n")
        
        
##    def promptUserForString(self, prompt):
##        self.prompt = self
##        self.prompt = input("Enter your name: ")
##        # implement promptUserForString here
##        
##        return self.prompt # be sure to change this
##
##    def promptUserForPositiveNumber(prompt):
##        self.prompt = prompt
##        self.prompt = eval(input("Enter a number: "))
##        if self.prompt < 0:
##            print("Amount cannot be negative.Try again")
##            promptUserForPositiveNumber(prompt)
##        else:
##            return float(self.prompt, 2)
##        # implement promptUserForPositiveNumber here
##        
##        return 0.0 # be sure to change this
##    
##    def generateRandomInteger(self, min, max):
##        self.min = min
##        self.max = max
##        return (random.randint(self.min, self.max))
##        
##        # implement generateRandomInteger here
##    
##    def convertFromDollarsToCents(self, amount):        
##        # implement convertFromDollarsToCents here     
##        self.amount = amount
##        return int(self.amount)
        
    
    '''
      Checks if a given string is a number (long)
      This does NOT handle decimals.
      
      YOU DO NOT NEED TO CHANGE THIS METHOD
      THIS IS FREE FOR YOU TO USE AS NEEDED
      
      @param numberToCheck String to check
      @return true if the String is a number, false otherwise
     '''
##    def isNumeric(numberToCheck):
##        try:
##            if numberToCheck.isdigit():
##                return True
##            else:
##                return False
##        except ValueError:
##            return False



class CoinCollector:

    # constructor so you cannot instantiate this class
    def __init__(self,coins):
        self.coins = coins
        

    def parseChange(self, coins):
       
        self.coins = coins
        # implement parseChange here
        #Takes 1 parameter, a String that represents a set of coins
        #Write 3 unit tests for this function
        Change_stack = iter(self.coins)
        Coin_Dir = {'P': 0.01, 'N': 0.05,
                    'D': 0.10, 'Q': 0.25, 'H': 0.50,
                    'W': 1.00}
        Total_Coins = 0
        
        for i in Change_stack:
            try:
                Total_Coins  += Coin_Dir[i]
            except:
                print("Invalid coin: i")
            
            return Total_Coins


if __name__== "__main__":
    main()


