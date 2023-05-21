import random



class Bank:
    
    
        
    def __init__(self):
    
               
        self.database = []#This is a class attribute is initialized to an empty list
        
    #This method acts soley on the class attribute database to update the list of Account objects.
    #this function should capture up to 100 client accounts, each element is an account object with retrievable attributes initialized in the Account class.
    #if an element in the list is 'null' that object is added to the list.
    
    def addAccountToBank(self, acc_object):

        if len(self.database) < 100:
            self.database.insert(0, acc_object)
            return True
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
       

class Account:

    def __init__(self):
        #These attributes are initialized everytime this class is instantiated.
        Utility = BankUtility()
        self.Account_number = ''.join(map(str,Utility.generateRandomInteger(0,9,8))) #This number is generated randomly whenever an Account instance is created
        self.first_nam = None
        self.Last_nam = None
        self.SSN = None
        self.PIN = ''.join(map(str,Utility.generateRandomInteger(0,9,4))) #This number is generated randonly whenever an Account instance is created.
        self.Balance = None
        
    def set_first_nam (self, new_name):
        self.first_nam = new_name

    def set_Last_nam(self, new_surname):
        self.Last_nam = new_surname

    def set_SSN(self, SS_number):
        self.SSN = SS_number

    def set_Balance(self, Start_Balance):
        self.Balance = Start_Balance
    
    def setPIN(self, Pin_set, Customer_acc):#This function takes two parameters, the new PIN and the customer account(An Account object) and then sets the PiN
        #on the account.
        Customer_acc.PIN = Pin_set
        return True
        
    def toString(self):
        #returns a string that contains the names and values of all the attributes
        print(f"Account Number: {self.Account_number}\n", f"Owner's First Name: {self.first_nam}\n", f"Owner's Last Name: {self.Last_nam}\n",
              f"Owner's SSN: {self.SSN}\n", f"PIN: {self.PIN}\n", f"Balance: {self.Balance}\n")
        
        
    def deposit(self, add_sum, balance):#An attribute deposit_object(An Account object) was added
        #so that the correct account balance could returned.
        balance = float(balance) + float(add_sum)
        return balance

    def withdraw(self, withdrawal_amt, withdrawal_acc_bal):# An attribute withdrawal_object was added
        #so that the corrent balance could be returned.
       if float(withdrawal_acc_bal) < float(withdrawal_amt):
           print("Insufficient Funds")
       else:
           withdrawal_acc_bal = float(withdrawal_acc_bal) - float(withdrawal_amt)
           return withdrawal_acc_bal
        
        
        
##   def isValidPIN(self, pin): #This function checks for a valid PIN
##        self.pin = pin


class BankUtility:

    def __init__(self):
        self

    def isNumeric(self,numberToCheck):
        if isinstance(numberToCheck, int):
            return True
        else:
            return False

    def promptUserForString(self, Short_String):
        Select_option = input(Short_String)
        return Select_option
        
    def promptUserForPositiveNumber(self, String):
        a = int(input(String))
        if a <= 0:
            print("Number cannot be negative.Try again")
        else:    
            return a
        
    def convertFromDollarsToCents(self, amount):        
        # implement convertFromDollarsToCents here     
        self.amount = amount
        return int(amount)    

    def generateRandomInteger(self, min, max, num):
        return random.choices((min, max), k = num)



class CoinConverter:

     # constructor so you cannot instantiate this class
    def __init__(self,coins):
        self.coins = coins 
        

    def parseChange(self, coins):
       
        
        # implement parseChange here
        #Takes 1 parameter, a String that represents a set of coins
        #Write 3 unit tests for this function
        Change_stack = iter(coins)
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





class BankManager(Bank, Account, BankUtility):
    
    def __init__(self):

        Bank.__init__(self) 
        Account.__init__(self)
        BankUtility.__init__(self)

    def main(self):

        User_Selection = """What do you want to do?\n\n 
        1. Open an account \n
        2. Get account information and balance\n
        3. Change PIN\n
        4. Deposit money in account\n
        5. Transfer money between accounts\n
        6. Withdraw money from account\n
        7. ATM withdrawal\n
        8. Deposit change\n
        9. Close an account\n
        10. Add monthly interest to all accounts\n
        11. End Program\n"""

        Name1 = 'Enter Account Owner\'s First Name: '
        Name2 = 'Enter Account Owner\'s Last Name: '
        Social = 'Enter Account Owner\'s SSN: '
             
        ClientManager = Bank() #This is a Bank object that should initialize  a database
        Startup = BankUtility() #This is a BankUtility object will need attributes for Bank and BankUtility
            
        
        ATM_Feature = Startup.promptUserForPositiveNumber(User_Selection)

        while (Startup.isNumeric (ATM_Feature)) is False:
            print("Invalid Entry")
            ATM_Feature = Startup.promptUserForPositiveNumber(User_Selection)
            
        while ATM_Feature > 11:
            print("Invalid Entry")
            ATM_Feature = Startup.promptUserForPositiveNumber(User_Selection)
            
        
        while ATM_Feature <= 11:      
            #This feature should open a new account and add that account to the database in the Bank class. Once the attributes in the Account class has been set, they are all printed by the toString
            #function in the account class.
            if ATM_Feature == 1:
            
                print("OPEN ACCOUNT\n")
                First_Nam = Startup.promptUserForString(Name1)
                Last_Nam = Startup.promptUserForString(Name2)
                SS = Startup.promptUserForString(Social)
                Starting_balance = '0.00'

                
                new_Client_Account = Account()
                new_Client_Account.set_first_nam(First_Nam)
                new_Client_Account.set_Last_nam(Last_Nam)
                new_Client_Account.set_SSN(SS)
                new_Client_Account.set_Balance(Starting_balance)

                ClientManager.addAccountToBank(new_Client_Account) #Adds Account object to the database located in the Bank class.

                new_Client_Account.toString() #ClientManager.addAccountToBank(Client_Account)
                ATM_Feature = Startup.promptUserForPositiveNumber(User_Selection)
                        
            elif ATM_Feature == 2:
                
                get_Client_data = BankManager.PromptForAccountNumberAndPin(object, ClientManager.database )
                get_Client_data.toString()
                ATM_Feature = Startup.promptUserForPositiveNumber(User_Selection)
            
            elif ATM_Feature == 3:#This feature prompts the user to enter their account number and the corresponding PIN.

                Client_Account = Account()
                Pin_change = BankManager.PromptForAccountNumberAndPin(object,ClientManager.database) #This command line returns an Account object
                #User is prompted to enter a new PIN    
                New_PIN = input("Enter new PIN (must be 4 digits): \n")
                while len(New_PIN) < 4:
                    New_PIN = input("Enter new PIN (must be 4 digits): \n") 
                Confirm_PIN = input("Confirm new PIN: \n")
                while New_PIN != Confirm_PIN:
                    Confirm_PIN = input("PINs did not match \n Confirm new PIN: \n")
                if Client_Account.setPIN(Confirm_PIN, Pin_change) is True:
                
                    print("PIN updated\n Thank you!")
                    ATM_Feature = Startup.promptUserForPositiveNumber(User_Selection) #This reprints the main menu for the user to continue doing transactions

                #This feature requests a deposit amount. The user is prompted for the Account Number and the PIN
                #the database is searched, the Account object is returned and then Balance is updated by a setter function.            
            elif ATM_Feature ==4:

                Client_Account = Account()
                Deposit_account = BankManager.PromptForAccountNumberAndPin(object, ClientManager.database)
                Deposit = float(Startup.promptUserForPositiveNumber("Enter dollar amount to deposit:"))
                print("New Balance in", Deposit_account.Account_number, ": {}".format(Deposit_account.deposit(Deposit, Deposit_account.Balance)))
                ATM_Feature = Startup.promptUserForPositiveNumber(User_Selection) #This reprints the main menu for the user to continue doing transactions
                        
                #This feature should transfer money between accounts 
            elif ATM_Feature == 5:

                
                print("Account to Transfer From: ")
                From = BankManager.PromptForAccountNumberAndPin(object, ClientManager.database)
                
                print("Account to Transfer To: ")
                To = BankManager.PromptForAccountNumberAndPin(object, ClientManager.database)
                
                Transfer = float(Startup.promptUserForPositiveNumber("Enter dollar amount to transfer:"))
                        
                #The first command line withdraws the transfer amount from the 'From' account.
                #The second command line deposits the transfer amount to 'To'' account.
                print("Transfer Complete", "\n", "New Balance in Account", From.Account_number,"is: {}".format(From.withdraw(Transfer, From.Balance)),
                    "New Balance in Account", To.Account_number, "is: {}".format(To.deposit(Transfer, To.Balance))) 

                ATM_Feature = Startup.promptUserForPositiveNumber(User_Selection) #This reprints the main menu for the user to continue doing transactions

                #This feature should withdraw money from an account
            elif ATM_Feature == 6:

                
                        
                Withdraw_Account = BankManager.PromptForAccountNumberAndPin(object, ClientManager.database)
                
                Withdrawal_Total = int(Startup.promptUserForPositiveNumber("Enter a dollar amount to transfer:"))
                print("New Balance: ", Withdraw_Account.withdraw (Withdrawal_Total, Withdraw_Account.Balance))
                        
                ATM_Feature = Startup.promptUserForPositiveNumber(User_Selection) #This reprints the main menu for the user to continue doing transactions

            #This feature should make an ATM withdrawal form an account       
            elif ATM_Feature == 7:

                
                              
                ATM_Withdrawal = BankManager.PromptForAccountNumberAndPin(object, ClientManager.database)
                
                ATM_Amount = int(Startup.promptUserForPositiveNumber("Enter amount to withdraw in dollars (no cents) in multiples of 5(limit $1000):"))      
                Startup.ATM_CASH(ATM_Amount)#This function in BankUtility parses the amount
                #into multiples of $5
                print("New balance: ", ATM_Withdrawal.Balance)
                ATM_Feature = Startup.promptUserForPositiveNumber(User_Selection) #This reprints the main menu for the user to continue doing transactions

                #This feature deposits coins
            elif ATM_Feature == 8:

                
                Coin_deposit = BankManager.PromptForAccountNumberAndPin(object, ClientManager.database)
                                
                coins = Startup.promptUserForString("Deposit coins (e.g. P for a penny, N for nickel etc): ")
                CoinDrop = CoinConverter(coins)
                Coin_sum = CoinDrop.parseChange(coins)
                
                print("${}".format(CoinDrop.parseChange(coins)), "in coins deposited into Account","\n",
                "New Balance: $ {}".format(Coin_deposit.deposit(Coin_sum, Coin_deposit.Balance))) 
                ATM_Feature = Startup.promptUserForPositiveNumber(User_Selection) #This reprints the main menu for the user to continue doing transactions

                #This feature closes an account
            elif ATM_Feature == 9:

                Closure = BankManager.PromptForAccountNumberAndPin(object, ClientManager.database)
                

                if ClientManager.removeAccountFromBank(Closure.Account_number) == 'null':
                    print("Account not found for account number: ", Closure.Account_number)
                        
                              
                #The user is prompted to enter an account number
                Check_closure = input("Enter Account Number: ")
                ClientManager.findAccount(Check_closure)
                ATM_Feature = Startup.promptUserForPositiveNumber(User_Selection) #This reprints the main menu for the user to continue doing transactions

            #This feature adds an interest to the account balance after find the Account object
            elif ATM_Feature == 10:

                
                Add_Interest = BankManager.PromptForAccountNumberAndPin(object, ClientManager.database)#This returns a specigic Account object
                

                Interest_Rate = float(input("Enter annual interest rate percentage(e.g. 2.75 for 2.75%):"))
                ClientManager.addMonthlyInterest(Add_Interest.Account_number, Add_Interest.Balance, Interest_Rate)
                ATM_Feature = Startup.promptUserForPositiveNumber(User_Selection) #This reprints the main menu for the user to continue doing transactions
                    
            elif ATM_Feature == 11:
                print("Thank you! Goodbye")
                exit()
            

            
    def PromptForAccountNumberAndPin(self, bank_object):

        User_Account = input("Please enter your 8 digit account number: \n")
        for account in bank_object:
            while account.Account_number != User_Account:
                print("Account not found")
                User_Account = input("Please enter your 8 digit account number: \n")
            pin = input("Please enter your 4 digit PIN: \n")
            while pin != account.PIN:
                print("Invalid PIN")
                pin = input("Please enter your 4 digit PIN: \n")
            return account
            
                   
        
                
                



       
    
        

    

        

if __name__ == '__main__':
    BankManager.main(object)
