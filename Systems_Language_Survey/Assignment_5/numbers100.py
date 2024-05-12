#Name: Shawn Forrester
#Date: 02-21-2024
#Assignment 5

import os
import random
import sys

#method to create a folder
def createFolder(folderName):
    try:
        os.mkdir(folderName)
    except FileExistsError:
        os.rmdir(folderName)
        os.mkdir(folderName)

#method to create a file
def createFile(folderName):
    with open(f"{folderName}/numbers100.txt", "w") as file:
        for i in range(100):
            file.write(f"{random.randint(0, 1000)}\n")  

#main method
def main():
    folderName = input("Please enter the name of the folder to be created: ")
    createFolder(folderName)
    createFile(folderName)

if __name__ == "__main__":
    main()
    sys.exit(0)
