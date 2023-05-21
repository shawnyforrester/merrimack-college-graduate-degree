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