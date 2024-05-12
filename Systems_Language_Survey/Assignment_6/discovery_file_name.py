# Create a Python program that discovers the current OS and ask the user a file name with path and converts it according to the system.
# Your program should use the packages platform and os.
# Once your program is aware of the platform, ask the user a file name with the path (it can be entered according to any format - MacOS or Windows), and your program should convert it to the right format according to the platform and OS the program is running.
# Your program should use the packages platform and os.

#Name: Shawn Forrester
#Version: 3.10.6

import platform
import os


def convertFileName(filePath, current_platform):
    try:
        formattedPath = ""
        if(current_platform == "Windows"):
            formattedPath = os.path.normpath(filePath)
        elif(current_platform == "Darwin"):
            formattedPath = os.path.abspath(filePath)
        else:
            raise OSError("The current OS does not support this file path")
        return formattedPath
    except Exception as e:
        print(f"An error occurred: {e}")
        



def main():
    current_platform = platform.system()
    print(f"The current OS is: {current_platform}")
    fileName = input("Please enter the file name and complete path: ")
    formattedFileName = convertFileName(fileName, current_platform)

    if(formattedFileName ):
        print(f"The correct path for this file is: {formattedFileName}")    

if __name__ == "__main__":
    main()


    