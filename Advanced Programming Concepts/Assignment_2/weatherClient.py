# Name: Shawn Forrester
# Python Version: 3.10.11
# REST API Version: 1.0
# API:  https://api.weather.gov/ (v1.1)
# Description: This program is a client that will connect to the weather.gov API and retrieve the weather for a given location.
# The user will be prompted to enter a an office ID and grid locations X and Y.The program will return the current weather for that location in default GeoJSON format.

import datetime
import requests

# Function to get the weather for a given location
def getForecast():
    # Prompt the user to enter the office ID
    officeID = input("Enter the office ID (you may want to use PAH): ")
    # Prompt the user to enter the grid location X
    gridX = input("Enter the grid location X (a postive integer): ")
    # Prompt the user to enter the grid location Y
    gridY = input("Enter the grid location Y (a positive integer): ")

    # URL for the weather API
    url = "https://api.weather.gov/gridpoints/" + officeID + "/" + gridX + "," + gridY + "/forecast"

    # Send a GET request to the API
    response = requests.get(url)

    # Check if the response is successful
    if response.status_code == 200:
        # Get the JSON data from the response
        data = response.json()
        # Get the current weather from the JSON data        
        # Print the name, startTime(formatted to DD-MM-YYYY) and temperature for each period      
        for period in data["properties"]["periods"]:
            formattedDate = datetime.datetime.strptime(period["startTime"][:10], '%Y-%m-%d').strftime('%d-%m-%Y')
            print(period["name"] + " " + "(" + formattedDate + ")" + " "
                  + "the expected temperature is " + str(period["temperature"]) + " and ")
       
       
    else:
        # Print an error message if the response is not successful
        print("Error: Unable to get weather data")
        
# Call the getForecast function
getForecast()




