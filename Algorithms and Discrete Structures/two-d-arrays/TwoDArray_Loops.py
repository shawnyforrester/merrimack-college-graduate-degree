### the size of the 2 d array
##grid_size = 10
##
### this is the array declaration
##twoDarry = [ ['']*grid_size for i in range(grid_size) ]
##
### display the grid (2d array)
##def displayArray(thearray):
##    for i in range(grid_size):
##        for j in range(grid_size):
##            print(thearray[i][j], end = "")
##        print()
##        
### initilize the 2 d array (the grid)
##def setupArray(thearray):
##    i = j = 0
##    while i < grid_size:
##        while j < grid_size:
##            # store the string "i, j" into the array
##            thearray[i][j] = str(i) + "," + str(j) + " "
##            j += 1
##        j = 0
##        i += 1
##        
### the main function!
##def main(thearray):
##    # first set up the array
##    setupArray(thearray)
##    # now display the array
##    displayArray(thearray)
### don't forget to call the main function
### lastly do NOT forget to pass the array we declared
##main(twoDarry)


##from array import *
##
##a = ['apple', 'mango', 'banana']
##
##
##print(a[::-1])

##def main():
##    days = "MonTueWedThurFriSatSun"
##    d = int (eval(input("Pick a day of the week (1-7): ")))
##    fst = (d-1)*3
##    print(days[fst+1:fst+3], "is the", str(d)+ "-th day of the week")
##
##main ()

##print("This float {0:10.5} to precision".format(6))


##def main():
##    print("change COunter\n")
##
##    print("Please enter the count of each coin type.")
##    quarters = int(input("Quarters: "))
##    dimes = int(input("Dimes:" ))
##    nickels = int(input("Nicekls: "))
##    pennies = int(input("Pennies: "))
##
##    total = quarters * 25 + dimes * 10 + nickels * 5 + pennies
##
##    print ("The total value of your change is ${0}.{1:0>2}".format(total//100, total %100))
##
##main()

def main():
    choice = input("Enter 'e' to encode, or 'd' to decode: ")
    if (choice == "e"):
        text = input ("Enter the text to encode: \n")
        for c in text:
            print(ord(c), end=" ")
        print()
    else:
        code = input("Enter the code to decode: \n")
        ncode = code.split()
        for n in ncode:
            print(chr(eval(n)), end = " ")
            print()

main()




